import pytest

from russian_names import RussianNames


def test_batch():
    batch_size = 10
    batch = RussianNames(
        gender=0.9,
        name_max_len=10,
        count=batch_size,
        transliterate=True,
        patronymic_max_len=10,
        patronymic_reduction=True
    ).get_batch()
    assert len(batch) == batch_size


def test_generator():
    batch_size = 10
    names = RussianNames(
        count=batch_size,
        gender=0.2,
        transliterate=True,
        surname_max_len=10,
        patronymic=False,
        surname_reduction=True,
        seed=2324
    )
    names_len = len(names)
    x = 0
    for _ in names:
        x += 1
    assert x == batch_size
    assert names_len == batch_size


def test_formats():
    for out_format in ('dict', 'list', 'tuple', 'str'):
        names = RussianNames(
            count=10,
            transliterate=True,
            name_max_len=10,
            output_type=out_format,
            name_reduction=True
        )
        batch = names.get_batch()
        assert len(batch) == 10


def test_error_output_type():
    with pytest.raises(ValueError):
        names = RussianNames(
            count=10,
            transliterate=True,
            name_max_len=10,
            output_type='file',
            surname=False,
            name_reduction=True
        )
        batch = names.get_batch()
        name, patronym = batch[0].split(' ')
        assert len(name) == 10
        assert len(batch) == 10
