from .names import RussianNames
from .utils import load_data


__version__ = '0.1.2'
__author__ = 'Matt Stroganov'


data = load_data()
RussianNames.read_data(data)

__all__ = (
    '__version__',
    '__author__',
    'RussianNames',
)
