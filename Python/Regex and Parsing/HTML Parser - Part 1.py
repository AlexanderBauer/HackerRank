from html.parser import HTMLParser
import sys

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        if(attrs):
            for x in attrs:
                print('-> ' + str(x[0]) + ' > ' + str(x[1]))
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        if(attrs):
            for x in attrs:
                print('-> ' + str(x[0]) + ' > ' + str(x[1]))
    def handle_comment(self, data):
        pass

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(sys.stdin.read())