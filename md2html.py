#!/usr/bin/python3

import re
import hashlib


class MarkdownToHtml:
    """
    Markdown to HTML convertor class
    """

    def __init__(self, input_text=None, input_filename=None, output_filename=None):
        self.input_text = input_text
        self.input_filename = input_filename
        self.output_filename = output_filename

    @staticmethod
    def __convert(line):
        output = ""
        unordered_start, ordered_start, paragraph = False, False, False

        # bold syntax
        count = line.count('**')
        for ite in range(count // 2):
            line = line.replace('**', '<b>', 1)
            line = line.replace('**', '</b>', 1)

        count = line.count('__')
        for ite in range(count // 2):
            line = line.replace('__', '<em>', 1)
            line = line.replace('__', '</em>', 1)

        # Handle md5
        md5 = re.findall(r'\[\[.+?\]\]', line)
        md5_inside = re.findall(r'\[\[(.+?)\]\]', line)
        if md5:
            line = line.replace(md5[0], hashlib.md5(
                md5_inside[0].encode()).hexdigest())

        # remove the letter (())
        remove_doubled_parentheses = re.findall(r'\(\(.+?\)\)', line)
        remove_more_parentheses = re.findall(r'\(\((.+?)\)\)', line)
        if remove_doubled_parentheses:
            remove_more_parentheses = ''.join(
                c for c in remove_more_parentheses[0] if c not in 'Cc')
            line = line.replace(remove_doubled_parentheses[0], remove_more_parentheses)

        length = len(line)
        headings = line.lstrip('#')
        heading_num = length - len(headings)
        unordered = line.lstrip('-')
        unordered_num = length - len(unordered)
        ordered = line.lstrip('*')
        ordered_num = length - len(ordered)

        # Handle headings
        if 1 <= heading_num <= 6:
            line = '<h{}>'.format(
                heading_num) + headings.strip() + '</h{}>\n'.format(
                heading_num)

        # Handle lists
        if unordered_num:
            if not unordered_start:
                output += '<ul>\n'
                unordered_start = True
            line = '<li>' + unordered.strip() + '</li>\n'

        if unordered_start and not unordered_num:
            output += '</ul>\n'
            unordered_start = False

        if ordered_num:
            if not ordered_start:
                output += '<ol>\n'
                ordered_start = True
            line = '<li>' + ordered.strip() + '</li>\n'

        if ordered_start and not ordered_num:
            output += '</ol>\n'
            ordered_start = False

        if not (heading_num or unordered_start or ordered_start):
            if not paragraph and length > 1:
                output += '<p>\n'
                paragraph = True
            elif length > 1:
                output += '<br/>\n'
            elif paragraph:
                output += '</p>\n'
                paragraph = False

        if length > 1:
            output += line

        if unordered_start:
            output += '</ul>\n'
        if ordered_start:
            output += '</ol>\n'
        if paragraph:
            output += '</p>\n'

        return output

    def convert_text(self):
        return self.__convert(self.input_text)

    def convert_input(self):
        output = ""
        line = input()
        while line:
            output += self.__convert(line)
            line = input()

        return output

    def convert_file(self):
        with open(self.input_filename) as read:
            with open(self.output_filename, 'w') as html:
                for line in read:
                    output = self.__convert(line)
                    html.write(output)
