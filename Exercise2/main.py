import json

# Load data from source
with open("source.json", "r") as f:
    input = json.load(f)


# Converter function that converts json to html
def json_converter(data_input):
    output = ""
    for key, value in data_input.items():
        output += "<" + str(key) + ">" + str(value) + "<" + "/" + str(key) + ">"
    return output

# Call converter, add returned data to final output
final_output = ""
for i in range(len(input)):
    final_output += json_converter(input[i])

# Update/Create index.html with new data
with open("index.html", "w") as w:
    w.write(final_output)
