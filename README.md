# Fic Poisoner

A small script that injects random, garbage words into an Ao3 fic, or any piece of HTML-formatted text.  Junk text uses HTML classes that can be hidden with CSS.

This program requires that you have ([downloaded Python](https://www.python.org/downloads/)) so that you can run the necessary script.  If you don't want to download Python, try the [online version](https://tricksofloki.github.io/ficpoison.html) instead.

### Preparing your fic

Always keep a backup of your unpoisoned fic, in case you need to revert or make changes later.

Go to Ao3's skins page.  Either create a new work skin, or edit the skin currently being used for your fic.  Add this section of code to the skin and save it:

```
#workskin .poison {
  display: none;
}
```

Go to your fic's edit page.  Make sure that the work skin you just edited is selected for your fic in the Associations section.  Scroll down to the Work Text section, and ensure that the HTML option is selected, *not* Rich Text.  Copy the entire work or chapter, and paste it into a text document on your computer.  Save the document somewhere you can easily find it again, ideally in the same folder as `add_poison.py`.

If you're copy and pasting a new work from another source, you can paste into the Rich Text editor and then switch to HTML, to allow Ao3 to automatically format your text.

### Poisoning

There are two methods for applying poison to your fic.  Both options will create a duplicate text file, with the same name as the original and "_poisoned" appended on the end, with your poisoned fic inside.

#### Option One: Right-click, Open with

For a simple, straightforward experience, use this option.

Find `add_poison.py`, right-click it, and hover over the "Open with" option.  If Python is not listed as an option, select "Choose another app" and find Python.  When the program opens, you should be prompted to enter the name of your unpoisoned fic file, as well as a few additional options.

#### Option Two: Command Line

For a streamlined method more suited to quickly poisoning multiple pieces of text in a row, use this option.

Use a command line to run `add_poison.py` as a Python file with the arguments listed below.

Run options:

- `filepath`: Required, the path to the file with your HTML-formatted fic.
- `-m`, `--mode`: Optional, which mode to use.  `default` mode inserts single words randomly throughout the text.  `tame` mode adds one paragraph of junk text in between each normal paragraph.
- `-c`, `--class`: Optional, name of the class to be used.  Defaults to `poison`.  **Remember to update your Ao3 work skin if you change this.**

### Updating/publishing your fic

Copy the text from the newly generated file back into the HTML editor (*not* the Rich Text editor).  Remember to preview your fic to make sure that everything is working correctly before updating or publishing.

You should also add an author's note letting readers know that native Ao3 downloads won't work correctly, and they should instead save the page through their browser if they want to read offline.  AI scrapers aren't likely to bother checking the author's notes for every fic they scrape, so it should be safe to explain to your readers.  Alternatively, you can [save a copy of your fic's Ao3 page on the Wayback Machine](https://help.archive.org/help/save-pages-in-the-wayback-machine/) *before* applying poison, which should allow people to download clean copies from the archived version.

#### Thanks to dolph for the word list from [their GitHub](https://github.com/dolph/dictionary)

(Note: I have attempted to remove all notable swears, slurs, and other offensive language from the word list.  If you think I missed anything, please send a message to [my Tumblr ask box](https://www.tumblr.com/new/ask/all-hail-trash-prince) and I will remove any offending words.)