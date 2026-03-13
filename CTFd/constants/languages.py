from CTFd.constants import RawEnum


class Languages(str, RawEnum):
    UKRAINIAN = "uk"


LANGUAGE_NAMES = {
    "uk": "Українська мова",
}

SELECT_LANGUAGE_LIST = [("", "")] + [
    (str(lang), LANGUAGE_NAMES.get(str(lang))) for lang in Languages
]

Languages.names = LANGUAGE_NAMES
Languages.select_list = SELECT_LANGUAGE_LIST
