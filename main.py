import md2html
from reverse_text import ReverseText

md2html.MarkdownToHtml(input_filename="README.md", output_filename="HTML.html").convert()

text = input('Enter the text here: ')

reverseText = ReverseText(text)

print(reverseText.reverse_character_wise())
print(reverseText.reverse_character_wise_o1())
print(reverseText.reverse_word_wise())
