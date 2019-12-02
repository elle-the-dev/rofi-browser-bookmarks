from rofi_browser_bookmarks.ChromeBookmarksParser import ChromeBookmarksParser
from rofi_browser_bookmarks.BrowserNotFoundException import BrowserNotFoundException

class BookmarksParserFactory:
    def make(self, browser: str):
        if (browser == 'google-chrome'):
            return ChromeBookmarksParser()

        raise BrowserNotFoundException()
