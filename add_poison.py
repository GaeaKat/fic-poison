# Adds junk text in an attempt to make fics unuseable to train AI
# By TricksOfLoki
# Updated 8/23/2026

from io import open
from sys import argv
from os.path import exists, isfile
from random import randint
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("filename", default="fic.txt", type=str, help="input file location")
    parser.add_argument("-m", "--mode", default="default", help="tame or default")
    parser.add_argument("-c", "--class", default="poison", type=str, help="poison class name (default: poison)")

    args = parser.parse_args()
    config = vars(args)

    return config["filename"] or None, config["mode"] or None, config["class"] or None


def add_poison(filename:str, mode:str, poison_class:str):

    # Get word list
    listpath = argv[0][0:-13] + "popular.txt"
    with open(listpath, mode="r") as file:
        words = file.read()
        words = words.split("\n")
        wordslen = len(words)

    if mode == "tame":
        # Get fic stored in HTML format
        with open(filename, mode="r", encoding="utf-8") as file:
            content = file.read()

        # Add a paragraph of junk text between every regular paragraph
        split = content.split("</p>")
        split.pop(len(split)-1) # Remove final empty item
        if len(split) <= 3:
            print("Your text wasn't able to be split into very many paragraphs. You may want to try default mode instead")
        content = ""
        for item in split:
            content += f"{item}</p>\n"
            junk = ""
            for i in range(0, randint(10, 100)):
                junk += words[randint(0, wordslen)] + " "
            content += f"<p class=\"{poison_class}\">{junk}</p>"
        return content

    elif mode == "default":
        # Get fic stored in HTML format
        with open(filename, mode="r", encoding="utf-8") as file:
            content = ""
            next_char = " "
            counting = True
            count = 1

            # Add spans of junk text at random intervals
            while True:
                next_char = file.read(1)
                if not next_char:
                    break
                content += next_char

                if next_char == "<" or next_char == "&":
                    counting = False
                elif next_char == ">" or next_char == ";":
                    counting = True

                if counting:
                    count -= 1
                if count <= 0:
                    junk = words[randint(0, wordslen)]
                    content += f"<span class=\"{poison_class}\">{junk}</span>"
                    count = randint(5, 50)
                
        return content
    
    else:
        raise Exception("Invalid mode. Try tame or default")


if __name__ == "__main__":
    try:
        if len(argv) > 1:
            filename, mode, poison_class = parse_args()
        else:
            print("Please enter your options here (leave empty for default)")
            filename = input("Filename (Default: fic.txt)\n> ") or "fic.txt"
            mode = input("Mode (Default: default)\n\
Options:\n\
 - default: adds individual hidden words randomly within the text\n\
 - tame: adds large paragraphs of hidden text after each existing paragraph\n> ") or "default"
            poison_class = input("Poison class name (Default: poison)\n\
Make sure to edit your Ao3 workskin to reflect the new class name if you use something other than the default!\n>") or "poison"
            
        # Check that input file exists
        if not exists(filename) or not isfile(filename):
            filename = argv[0][0:-13] + filename # try to find full filepath if relative path was given
        if not exists(filename) or not isfile(filename):
            raise Exception("Invalid file name. Make sure file name is correct, or try including the full file path")

        content = add_poison(filename, mode, poison_class)

        # Save new file next to old one
        new_filename = filename.replace(".txt", "_poisoned.txt")
        with open(new_filename, mode="w", encoding="utf-8") as new_file:
            new_file.write(content)
        print(f"\nSuccess!\nSaved to {new_filename}")
    except Exception as e:
        print("\nUh oh! Something went wrong.")
        print(e)

input("Press Enter to close window")