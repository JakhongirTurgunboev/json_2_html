from json2html import *
import json

# Getting data from source
with open("source.json", "r") as i:
        input = json.load(i)

# Converting json to html
output = json2html.convert(json=input)

# Saving html to a file
with open("index.html", "w") as f:
        f.write(output)
