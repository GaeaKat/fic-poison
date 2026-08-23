# Helper file to convert popular.txt into a list in a JS file for the web version. Feel free to ignore this :)

from io import open

with open("popular.txt", mode="r") as file:
    words = file.read()
    words = words.split("\n")
    print(f"{len(words)} words")

    content = "// Original list from: https://github.com/dolph/dictionary\nconst popular_list = [\n"
    for word in words:
        content += f"\"{word}\",\n"
        content.removesuffix(",\n")
    content += "]"

    with open("popular_list.js", mode="w") as file:
        file.write(content)
    
    print("done")