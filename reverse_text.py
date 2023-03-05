# This is a sample Python script.

def reverse_character_wise(input_text: str) -> str:
    reversed_text = ''

    for index in range(len(input_text) - 1, -1, -1):
        reversed_text = reversed_text + input_text[index]

    return reversed_text


def reverse_character_wise_o1(input_text: str) -> str:
    return input_text[::-1]


def reverse_word_wise(input_text: str) -> str:
    reversed_text = ''

    input_text = list(input_text)
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
    print(reverse_character_wise(text))
    print(reverse_character_wise_o1(text))
    print(reverse_word_wise(text))

