import unittest
from find_artworks import extract_artworks_info

class TestExtractArtworksInfo(unittest.TestCase):

    def test_extract_artworks_info(self):
        # Test with a sample HTML file
        # path_to_file = "./static-html/pablo_paintings.html"
        # art_work_div_classname = "iELo6"
        # img_attribute_name = "src"
        # div_classname_with_name = "pgNMRc"
        # div_classname_with_extensions = "cxzHyb"
        
        path_to_file = "../files/van-gogh-paintings.html"
        art_work_div_classname = "klitem"
        img_attribute_name = "data-src"
        div_classname_with_name = "kltat"
        div_classname_with_extensions = "ellip klmeta"

        # Call the function
        artworks_info = extract_artworks_info(path_to_file, art_work_div_classname, img_attribute_name, div_classname_with_name, div_classname_with_extensions)

        # Assert that artworks_info is not empty
        self.assertTrue(artworks_info)

        # Assert properties for each artwork_info object
        for artwork_info in artworks_info:
            self.assertIsInstance(artwork_info, dict)

            # Assert that the required properties are present and are of type string
            self.assertIn("name", artwork_info)
            self.assertIsInstance(artwork_info["name"], str)

            self.assertIn("link", artwork_info)
            self.assertIsInstance(artwork_info["link"], str)

            self.assertIn("image", artwork_info)
            self.assertIsInstance(artwork_info["image"], (str, type(None)))

            # Assert that the "extensions" property is optional and if exist, it is list
            if "extensions" in artwork_info:
                self.assertIsInstance(artwork_info["extensions"], list)

if __name__ == '__main__':
    unittest.main()

