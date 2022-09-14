import json

# Load data from source
with open("source.json", "r") as f:
    input = json.load(f)


# Converter function that converts json to html
def json_converter(data_input):
    output = ""
    for key, value in input.items():
        k = str(key)
        v = str(value)
        if "#" in key:
            id_key = k.split("#")[1]
            print(id_key)
        keys = k.split(".")
        print(keys)
        key_tag = keys[0]
        print(key_tag)
    return output

# Call converter, add returned data to final output
final_output = ""
final_output += json_converter(input)
# Update/Create index.html with new data
with open("index.html", "w") as w:
    w.write(final_output)
