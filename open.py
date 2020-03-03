import os
import time
import sys

import json

import subprocess

os.chdir('C:\\scripts')

argument = sys.argv[1]

input_file = open ('file-list.json')
json_array = json.load(input_file)

for item in json_array:
	name = item.get('name')
	item_dir = item.get('dir')

	if argument == name:
		subprocess.call("explorer " + item_dir, shell=True)
