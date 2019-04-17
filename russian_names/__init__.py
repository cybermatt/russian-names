from .names import RussianNames
from .utils import load_data


__version__ = '0.1.0'
__author__ = 'cybermatt'


data = load_data()
RussianNames.read_data(data)

__all__ = (
    '__version__',
    '__author__',
    'RussianNames',
)
