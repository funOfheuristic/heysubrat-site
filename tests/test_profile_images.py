import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"


class ImageCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))

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


if __name__ == "__main__":
    unittest.main()
