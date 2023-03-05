import unittest

from reverse_text import ReverseText


class ReverseTextTest(unittest.TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def testUp(self):
        print("setUp: Run once for every test method to setup clean data.")

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


if __name__ == '__main__':
    unittest.main()
