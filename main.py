from md2html import MarkdownToHtml
from reverse_text import ReverseText

# MarkdownToHtml(input_filename="README.md", output_filename="HTML.html").convert_file()
#
# print(MarkdownToHtml(input_text="###### h6 Heading").convert_text())
# output = MarkdownToHtml(output_filename="HTML.html").convert_input()
# print(output)

text = 'Enter the text here:'

reverseText = ReverseText(text)

print(reverseText.reverse_word_wise())
print(reverseText.reverse_text_pure())
