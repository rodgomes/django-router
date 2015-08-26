import unittest
from router import Parser

class TestURLConfigMethods(unittest.TestCase):

    def test_create_basic_url(self):
        urls = Parser.to_urls('test_router.cfg')
        self.assertIsNotNone(urls)

if __name__ == '__main__':
    unittest.main()
