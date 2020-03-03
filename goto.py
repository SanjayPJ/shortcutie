import os
import time
import webbrowser
import sys

import json

os.chdir('C:\\scripts')

argument = sys.argv[1]

input_file = open ('url-list.json')
json_array = json.load(input_file)

for item in json_array:
	name = item.get('name')
	item_url = item.get('url')

	if argument == name:
	    webbrowser.open(item_url)
