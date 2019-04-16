from russian_names.utils import transliterate_word, create_patronymics, \
    patronymic_from_name, check_suffix


def test_transliterate_word():
    assert transliterate_word('балалайка') == 'balalayka'
    assert transliterate_word('борода') == 'boroda'
    assert transliterate_word('щи') == 'schi'


def test_check_suffix():
    assert check_suffix('Воронцов') == 'Воронцов'
    assert not check_suffix('Джонсон')


def test_patronymic_from_name():
    assert patronymic_from_name('Иван', 'male') == 'Иванович'
    assert patronymic_from_name('Иван', 'female') == 'Ивановна'
    assert patronymic_from_name('Никита', 'male') == 'Никитич'
    assert patronymic_from_name('Никита', 'female') == 'Никитична'
    # assert patronymic_from_name('Евгений', 'male') == 'Евгеньевич'
    # assert patronymic_from_name('Артемий', 'female') == 'Артемьевна'


def test_create_patronymics():
    names = {'Федор', 'Алексей'}
    patronymics = {'Федорович', 'Алексеевич'}
    assert create_patronymics(names) == patronymics
