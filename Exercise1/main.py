import json

# Load data from source
with open("source.json", "r") as f:
    input = json.load(f)


# Converter function that converts json to html
def json_converter(data_input):
    output = ""
    for key, value in data_input.items():
        if key == "title":
            output += "<h1>" + str(value) + "</h1>"
        elif key == "body":
            output += "<p>" + str(value) + "<p>"
        else:
            raise KeyError

    return output

# Call converter, add returned data to final output
final_output = ""
for i in range(len(input)):
    final_output += json_converter(input[i])

# Update/Create index.html with new data
with open("index.html", "w") as w:
    w.write(final_output)
