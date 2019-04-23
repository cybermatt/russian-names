import zipfile
from os.path import abspath, join, dirname

from russian_names.consts import TRANSLITERATE_TABLE, SUFFIXES, PATRONYMIC_RULES


def transliterate_word(word):
    trans_word = ''
    for char in word:
        trans_word += TRANSLITERATE_TABLE.get(char, char)
    return trans_word


def check_suffix(word, suffixes=SUFFIXES):
    for suffix in suffixes:
        suffix_len = len(suffix)
        if word[-suffix_len:] == suffix:
            return word


def read_file(path_in, encoding='cp1251', length=None):
    f = open(path_in, 'r', encoding=encoding)
    words = f.read().splitlines()[:length]
    return words


def save_file(path_out, words, encoding='cp1251', sorting=False):
    if sorting:
        words.sort()
    with open(path_out, "w", encoding=encoding) as out_file:
        words_str = "\n".join(words)
        out_file.write(words_str)


def patronymic_from_name(name, gender='male'):
    """
    :param name: string
    :param gender: bool
    :return: string
    """
    last_char = name[-1]
    for rule, suffix in PATRONYMIC_RULES.items():
        cut, m_suffix,  w_suffix = suffix
        for char in rule:
            if last_char == char:
                if gender == 'male':
                    suffix = m_suffix
                else:
                    suffix = w_suffix
                return name[:-1] + suffix if cut else name + suffix


def create_patronymics(names):
    """
    Create patronymics from list of man names
    :param names: list
    :return: set
    """
    patronymics = set()
    for name in names:
        patronymic = patronymic_from_name(name)
        if patronymic:
            patronymics.add(patronymic)
    return patronymics


_BASE_PATH = '_data.zip'
_BASE_NAME = 'base.txt'


def load_data():
    path = abspath(join(dirname(__file__), _BASE_PATH))
    data_zip = zipfile.ZipFile(path)
    data = data_zip.read(_BASE_NAME)
    data_decoded = data.decode('utf8')
    return data_decoded.splitlines()


__all__ = (
    'load_data',
    'read_file',
    'save_file',
    'check_suffix',
    'transliterate_word',
)
