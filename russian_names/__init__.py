from .names import RussianNames
from .utils import load_data


data = load_data()
RussianNames.read_data(data)

__all__ = (
    'RussianNames',
)
