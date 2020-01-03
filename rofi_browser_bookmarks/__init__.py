from os import path
from subprocess import check_output, run, STDOUT
from subprocess import CalledProcessError
from sys import argv
from rofi_browser_bookmarks.BookmarksParserFactory import BookmarksParserFactory
from rofi_browser_bookmarks.BrowserNotFoundException import BrowserNotFoundException
from rofi_browser_bookmarks.FormatColumns import FormatColumns

def main():
    browser = None
    if len(argv) > 1:
        browser = argv[1]

    folder = None
    if len(argv) > 2:
        folder = argv[2]

    factory = BookmarksParserFactory()
    try:
        parser = factory.make(browser)
    except BrowserNotFoundException as e:
        print("Available browsers are: google-chrome")
        return

    options = FormatColumns().format(parser.parse(folder=folder))

    try:
        selection = check_output(['rofi', '-i', '-dmenu'], input=options.encode()).decode().strip()
        url = selection.split('\t')[1]
        run([browser, url])
    except CalledProcessError as e:
        pass
