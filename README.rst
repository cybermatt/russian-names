=============
russian-names
=============

Library for generation of russian names. Cyrillic and latin alphabet.
Useful for test, mocks etc.


Installation
============
Install with pip:

::

   $ pip install russian-names

Usage
=====
Import package:

::

   >>> from russian_names import RussianNames

Basic example
-------------
Print random name:

::

    >>> RussianNames().get_person()

    Владислав Николаевич Ильин

Batch
-----
Create batch of persons. Set size in *count* option.

::

    >>> rn = RussianNames(count=5, patronymic=False, name_reduction=True)
    >>> batch = rn.get_batch()
    >>> print(batch)

    ('Л. Ходилова', 'А. Креткова', 'Р. Тишанов', 'И. Закудряев', 'В. Демчин')


Generator
---------
Use russian names as generator

::

    >>> rn = RussianNames(count=7, patronymic=False, transliterate=True)
    >>> for person in rn:
            print(person)

        Valeriy Forunin
        Pavel Senakosov
        Violetta Scherbovskaya
        Natalya Furshtatova
        Violetta Chuhontseva
        Polina Aksentsova
        Galina Botova

Options
-------
List of options:

+----------------------+----------------------------+---------------------+---------+
| option               | description                | type                | default |
+======================+============================+=====================+=========+
| name                 |                            | bool                | True    |
+----------------------+----------------------------+---------------------+---------+
| name_reduction       | Anna -> A.                 | bool                | False   |
+----------------------+----------------------------+---------------------+---------+
| name_max_len         |                            | int                 | 10      |
+----------------------+----------------------------+---------------------+---------+
| patronymic           |                            | bool                | True    |
+----------------------+----------------------------+---------------------+---------+
| patronymic_reduction | Fedorovich -> F.           | bool                | False   |
+----------------------+----------------------------+---------------------+---------+
| patronymic_max_len   |                            | int                 | 10      |
+----------------------+----------------------------+---------------------+---------+
| surname              |                            | bool                | True    |
+----------------------+----------------------------+---------------------+---------+
| surname_reduction    | Ivanov -> I.               | bool                | False   |
+----------------------+----------------------------+---------------------+---------+
| surname_max_len      |                            | int                 | 10      |
+----------------------+----------------------------+---------------------+---------+
| count                |                            | int                 | 10      |
+----------------------+----------------------------+---------------------+---------+
| gender               |                            | float               | 0.5     |
+----------------------+----------------------------+---------------------+---------+
| transliterate        | cyrillic to latin          | bool                | False   |
+----------------------+----------------------------+---------------------+---------+
| output_type          |  output data format        | 'str' or 'list' or  | 'str'   |
|                      |                            | 'tuple' or 'dict'   |         |
+----------------------+----------------------------+---------------------+---------+
| seed                 | random seed                | int                 | None    |
+----------------------+----------------------------+---------------------+---------+
| rare                 | use non popular names      | bool                | False   |
+----------------------+----------------------------+---------------------+---------+
| uppercase            | set uppercase to all names | bool                | False   |
+----------------------+----------------------------+---------------------+---------+

Examples of options
-------------------
For credit cards:

::

    >>> RussianNames(count=3, patronymic=False, transliterate=True, uppercase=True).get_batch()
        ('SEMEN SISYKIN', 'LYBOV POLEZAEVA', 'MIHAIL KAMAGOROV')

For polls:

::

    >>> RussianNames(count=3, surname_reduction=True).get_batch()
        ('Анатолий Юрьевич Ш.', 'Софья Ивановна Т.', 'Валерия Валерьевна Н.')


Only women:

::

    >>> RussianNames(count=3, gender=0.0).get_batch()
        ('Кристина Петровна Тоншина', 'Клавдия Эдуардовна Караулова', 'Лариса Викторовна Короткина')

List of dicts:

::

    >>> RussianNames(count=3, output_type='dict').get_batch()
        (
            {'name': 'Кирилл', 'patronymic': 'Денисович', 'surname': 'Дрожжов'},
            {'name': 'Андрей', 'patronymic': 'Кириллович', 'surname': 'Шувиков'},
            {'name': 'Роман', 'patronymic': 'Евгеньевич', 'surname': 'Малеванкин'}
        )


Get current option
------------------
Print options

::

    >>> rn = RussianNames(count=10, gender=0.5, surname_max_len=15,
                          transliterate=True, uppercase=True)
    >>> print(rn)

        RussianNames settings:
             name: True
             name_reduction: False
             name_max_len: 10
             patronymic: True
             patronymic_reduction: False
             patronymic_max_len: 10
             surname: True
             surname_reduction: False
             surname_max_len: 15
             count: 10
             gender: 0.5
             transliterate: True
             output_type: str
             seed: None
             rare: False
             uppercase: True


Tests
=====

::

   $ pytest -v tests/*


License
=======

This project is licensed under the MIT License - see the LICENSE.txt_ file for details

.. _LICENSE.txt: LICENSE.txt
