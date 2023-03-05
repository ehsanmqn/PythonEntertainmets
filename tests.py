import unittest

from reverse_text import ReverseText
from md2html import MarkdownToHtml


class ReverseTextTest(unittest.TestCase):
    @classmethod
    def setUpTestData(cls):
        print("ReverseTextTest: Run once to set up non-modified data for all class methods.")
        pass

    @classmethod
    def setUp(cls) -> None:
        print("ReverseTextTest: Run for every test")

    def test_wordwise_reverse(self):
        test_text = "This is a test"
        test_reversed = "test a is This"

        reverse_text = ReverseText(test_text).reverse_word_wise()

        self.assertEqual(test_reversed, reverse_text)

    def test_character_wise(self):
        test_text = "This is a test"
        test_reversed = test_text[::-1]

        reverse_text = ReverseText(test_text).reverse_character_wise_o1()

        self.assertEqual(reverse_text, test_reversed)


class MarkdownToHtmlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("MarkdownToHtmlTest: Run once")

    @classmethod
    def setUp(cls) -> None:
        print("MarkdownToHtmlTest: Run for every test")


if __name__ == '__main__':
    unittest.main()
