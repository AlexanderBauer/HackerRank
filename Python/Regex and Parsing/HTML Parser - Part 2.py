from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        try:
            assert data.find('\n') > 0
        except:
            print('>>> Single-line Comment')
        else:
            print('>>> Multi-line Comment')
        finally:
            print(data)

    def handle_data(self, data):
        try:
            assert data != '\n'
        except:
            pass
        else:
            print(">>> Data")
            print(data)
            
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()