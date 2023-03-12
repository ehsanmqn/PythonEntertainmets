

# create a subclass and override the handler methods
class MyHTMLParser():

    def feed(self, data):
        self.examine_data(data, True)

    def examine_data(self, data, is_start):
        print(is_start)
        if len(data) == 0:
            return

        if data[0] == "<":
            tag = ""
            data.pop(0)
            character = data.pop(0)

            while character != ">":
                tag += character
                character = data.pop(0)

            if "/" in tag:
                tag = tag.replace("/", "")

                if is_start is False:
                    self.handle_endtag(tag=tag)
            else:
                self.handle_starttag(tag=tag)

            return self.examine_data(data, not is_start)

        while True:
            character = data[0]
            if character != "<":
                data.pop(0)
            else:
                break

        self.examine_data(data, not is_start)

    def handle_starttag(self, tag, attrs=None):
        print("Start  :", tag)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs=None):
        print(" :", tag)


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
data = "<html><head><title>HTML Parser - I</title></head>" + "<body><h1>HackerRank</h1><br /></body></html>"
parser.feed(list(data))

