import webbrowser
import sys

temp = sys.argv
temp.pop(0);

webbrowser.open("https://www.google.com/search?q=" + ' '.join(temp))