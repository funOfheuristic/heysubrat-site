import unittest
import struct
import zlib
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"


def read_png_rgba(path):
    data = path.read_bytes()
    offset = 8
    compressed = bytearray()
    width = height = None

    while offset < len(data):
        length = struct.unpack(">I", data[offset : offset + 4])[0]
        chunk_type = data[offset + 4 : offset + 8]
        chunk = data[offset + 8 : offset + 8 + length]
        offset += 12 + length

        if chunk_type == b"IHDR":
            width, height, bit_depth, color_type = struct.unpack(">IIBB", chunk[:10])
            if (bit_depth, color_type) != (8, 6):
                raise ValueError("Expected an 8-bit RGBA PNG")
        elif chunk_type == b"IDAT":
            compressed.extend(chunk)
        elif chunk_type == b"IEND":
            break

    raw = zlib.decompress(bytes(compressed))
    stride = width * 4
    rows = []
    previous = bytearray(stride)
    cursor = 0

    def paeth(left, above, upper_left):
        estimate = left + above - upper_left
        distances = (abs(estimate - left), abs(estimate - above), abs(estimate - upper_left))
        return (left, above, upper_left)[distances.index(min(distances))]

    for _ in range(height):
        filter_type = raw[cursor]
        cursor += 1
        encoded = raw[cursor : cursor + stride]
        cursor += stride
        row = bytearray(stride)

        for index, value in enumerate(encoded):
            left = row[index - 4] if index >= 4 else 0
            above = previous[index]
            upper_left = previous[index - 4] if index >= 4 else 0
            predictors = {
                0: 0,
                1: left,
                2: above,
                3: (left + above) // 2,
                4: paeth(left, above, upper_left),
            }
            row[index] = (value + predictors[filter_type]) & 0xFF

        rows.append(row)
        previous = row

    return width, height, rows


class ImageCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.links = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))
        if tag == "link":
            self.links.append(dict(attrs))

    def handle_data(self, data):
        content = data.strip()
        if content:
            self.text.append(content)


class ProfileImageTests(unittest.TestCase):
    def test_profile_photo_is_used_for_brand_hero_and_about(self):
        parser = ImageCollector()
        parser.feed((PUBLIC / "index.html").read_text(encoding="utf-8"))

        profile_images = [
            image for image in parser.images if image.get("src") == "subrat_image.png"
        ]
        self.assertEqual(len(profile_images), 3)
        self.assertTrue(any("brand-avatar-image" in image.get("class", "") for image in profile_images))
        self.assertTrue(any("hero-profile-image" in image.get("class", "") for image in profile_images))
        self.assertTrue(any("about-profile-image" in image.get("class", "") for image in profile_images))

        meaningful_alts = [image.get("alt") for image in profile_images if image.get("alt")]
        self.assertEqual(meaningful_alts, ["Subrat Mishra outdoors in a forest", "Subrat Mishra outdoors in a forest"])

    def test_profile_asset_is_a_valid_local_png(self):
        image = (PUBLIC / "subrat_image.png").read_bytes()
        self.assertTrue(image.startswith(b"\x89PNG\r\n\x1a\n"))

    def test_hero_does_not_show_the_build_move_make_overlay(self):
        parser = ImageCollector()
        parser.feed((PUBLIC / "index.html").read_text(encoding="utf-8"))

        self.assertFalse({"BUILD", "MOVE", "MAKE"}.intersection(parser.text))

    def test_browser_tab_uses_a_square_profile_favicon(self):
        parser = ImageCollector()
        parser.feed((PUBLIC / "index.html").read_text(encoding="utf-8"))

        icons = [link for link in parser.links if link.get("rel") == "icon"]
        self.assertEqual([icon.get("href") for icon in icons], ["images/favicon.png"])

        favicon_path = PUBLIC / "images" / "favicon.png"
        self.assertTrue(favicon_path.is_file())
        favicon = favicon_path.read_bytes()
        self.assertTrue(favicon.startswith(b"\x89PNG\r\n\x1a\n"))
        self.assertEqual(struct.unpack(">II", favicon[16:24]), (64, 64))

    def test_profile_favicon_has_a_round_transparent_mask(self):
        width, height, rows = read_png_rgba(PUBLIC / "images" / "favicon.png")

        corner_alpha = [
            rows[0][3],
            rows[0][(width - 1) * 4 + 3],
            rows[height - 1][3],
            rows[height - 1][(width - 1) * 4 + 3],
        ]
        center_alpha = rows[height // 2][(width // 2) * 4 + 3]

        self.assertEqual(corner_alpha, [0, 0, 0, 0])
        self.assertEqual(center_alpha, 255)


if __name__ == "__main__":
    unittest.main()
