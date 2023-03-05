# This is a sample Python script.


class ReverseText:
    def __init__(self, input_text: str) -> None:
        self.input = input_text

    def reverse_character_wise(self) -> str:
        reversed_text = ''

        for index in range(len(self.input) - 1, -1, -1):
            reversed_text = reversed_text + self.input[index]

        return reversed_text

    def reverse_character_wise_o1(self) -> str:
        return self.input[::-1]

    def reverse_word_wise(self) -> str:
        reversed_text = ''

        input_text = list(self.input)
        while True:
            word = ''
            character = input_text.pop()
            while character != ' ':
                word = word + character

                try:
                    character = input_text.pop()
                except IndexError as e:
                    character = ' '

            if len(input_text) > 0:
                reversed_text = reversed_text + word[::-1] + ' '
            else:
                reversed_text = reversed_text + word[::-1]
                return reversed_text


if __name__ == '__main__':
    text = input('Enter the text here: ')

    reverseText = ReverseText(text)

    print(reverseText.reverse_character_wise())
    print(reverseText.reverse_character_wise_o1())
    print(reverseText.reverse_word_wise())
