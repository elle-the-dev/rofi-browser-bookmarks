from os import path
from subprocess import check_output, run, STDOUT
from pathlib import Path
from subprocess import CalledProcessError
import json
import sqlite3

class FirefoxBookmarksParser:
    def parse(self, folder=None, file_path=None) -> str:
        # ~/.mozilla/firefox/[profile]/places.sqlite
        bookmarks_path = path.expanduser(file_path)

        if not path.isfile(bookmarks_path):
            print("No bookmarks file found!")
            exit()

        conn = sqlite3.connect(bookmarks_path)
        db = conn.cursor()
        query = """
            SELECT moz_places.id, moz_places.url, moz_bookmarks.title, moz_bookmarks.parent
            FROM moz_places
            JOIN moz_bookmarks
            ON moz_places.id = moz_bookmarks.fk
        """

        if folder is not None:
            response = db.execute("SELECT id FROM moz_bookmarks WHERE title = ?", (folder,))
            row = response.fetchone()
            folderId = row[0]
            query = query + " WHERE moz_bookmarks.parent = ?"
            rows = db.execute(query, (folderId,))
        else:
            rows = db.execute(query)

        options = ""
        for row in rows:
            title = row[2]
            if title is None:
                title = row[1]
            options = options + title + "\t" + row[1] + "\n"

        return options
