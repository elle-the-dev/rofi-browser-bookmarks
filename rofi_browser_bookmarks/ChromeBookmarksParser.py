from os import path
from subprocess import check_output, run, STDOUT
from pathlib import Path
from subprocess import CalledProcessError
import json

class ChromeBookmarksParser:
    def parse(self, folder=None) -> str:
        bookmarks_path = path.expanduser("~") + "/.config/google-chrome/Default/Bookmarks"

        if not path.isfile(bookmarks_path):
            print("No bookmarks file found!")
            exit()

        bookmarks_json = Path(bookmarks_path).read_text()
        bookmarks = json.loads(bookmarks_json)

        options = ""
        for items in bookmarks['roots']['bookmark_bar']['children']:
            if (not folder or items['name'] == folder):
                if 'children' in items:
                    for bookmark in items['children']:
                        if 'url' in bookmark:
                            options = options + bookmark['name'] + "\t" + bookmark['url'] + "\n"

        return options
