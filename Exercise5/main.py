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

        id_key = ""
        class_key = ""
        keys = k
        if "#" in k:
            id_key = k.split("#")[1]
            keys = k.split("#")[0]
        keys = keys.split(".")
        key_tag = keys[0]
        for i, c in enumerate(keys):
            if "class" in c:
                class_key += c
                if i != len(keys) - 1:
                    class_key += " "
        output += "<" + key_tag
        if id_key != "":
            output += " id=\"" + id_key + "\""
        if class_key != "":
            output += " class=\"" + class_key + "\""
        if "<" in v:
            v = v.replace("<", "&lt;")
        if ">" in v:
            v = v.replace(">", "&gt;")
        output += ">" + v
        output += "</" + key_tag + ">"
    return output

# Call converter, add returned data to final output
final_output = json_converter(input)
# Update/Create index.html with new data
with open("index.html", "w") as w:
    w.write(final_output)
