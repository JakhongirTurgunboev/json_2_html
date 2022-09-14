import json

# Load data from source
with open("source.json", "r") as f:
    input = json.load(f)


# Converter function that converts json to html
def json_converter(data_input):
    output = "<li>"
    for key, value in data_input.items():
        if isinstance(value, list):
            output += "<" + str(key) + ">" + "<ul><li>"
            for k, v in value[0].items():
                output += "<" + str(k) + ">" + str(v) + "<" + "/" + str(k) + ">"
            output += "<" + "/" + str(key) + ">" + "</li></ul>"
        else:
            output += "<" + str(key) + ">" + str(value) + "<" + "/" + str(key) + ">"
    output += "</li>"
    return output

# Call converter, add returned data to final output
final_output = "<ul>"
for i in range(len(input)):
    final_output += json_converter(input[i])
final_output += "</ul>"
print(final_output)
# Update/Create index.html with new data
with open("index.html", "w") as w:
    w.write(final_output)