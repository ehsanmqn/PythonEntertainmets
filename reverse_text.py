from importlib.resources import read_text


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

    def reverse_text_pure(self):

        input_text = list(self.input)
        reversed_text = [''] * len(self.input)

        end_index = len(input_text)
        start_index = end_index - 1
        reversed_index = 0

        while True:
            while input_text[start_index] != ' ' and start_index >= 0:
                start_index -= 1

            for index in range(start_index + 1, end_index):
                reversed_text[reversed_index] = input_text[index]
                reversed_index += 1

            if start_index <= 0:
                return ''.join(reversed_text)

            reversed_text[reversed_index] = ' '
            reversed_index += 1

            end_index = start_index
            start_index -= 1

