import random

from russian_names.utils import transliterate_word


class RussianNames:

    _data = []
    __slots__ = (
        'name', 'name_reduction', 'name_max_len', 'patronymic',
        'patronymic_reduction', 'patronymic_max_len', 'surname',
        'surname_reduction', 'surname_max_len', 'count', 'gender',
        'transliterate', 'output_type', 'seed', 'rare', 'uppercase',
        '_base',
    )

    def __init__(self, **kwargs):

        prop_defaults = {
            'name': True,
            'name_reduction': False,
            'name_max_len': 10,
            'patronymic': True,
            'patronymic_reduction': False,
            'patronymic_max_len': 10,
            'surname': True,
            'surname_reduction': False,
            'surname_max_len': 10,
            'count': 10,
            'gender': 0.5,
            'transliterate': False,
            'output_type': 'str',
            'seed': None,
            'rare': False,
            'uppercase': False,
        }

        seed = kwargs.pop('seed', None)
        if seed is not None:
            random.seed(seed)

        for prop, default in prop_defaults.items():
            setattr(self, prop, kwargs.get(prop, default))

        self._fill_base()

    def __str__(self):
        info = '{} settings:\n'.format(self.__class__.__name__)
        for option in self.__slots__:
            if option.startswith('_'):
                continue
            value = getattr(self, option)
            info += '\t {}: {}\n '.format(option, value)
        return info

    def __len__(self):
        return self.count

    def __iter__(self):
        while self.count:
            yield self.get_person()
            self.count -= 1

    @classmethod
    def read_data(cls, data):
        cls._data = data

    def _set_options(self, **kwargs):
        refill_base = False
        for prop, value in kwargs.items():
            if prop.endswith('_len'):
                refill_base = True
            setattr(self, prop, value)
        if refill_base:
            self._fill_base()

    def _load_set(self, section, max_len):
        return list(filter(lambda x: len(x) <= max_len, section.split(' ')))

    def _fill_base(self):
        self._base = {}
        names_m_r = self._data[0]
        names_m = self._data[1]
        patronymics_m_r = self._data[2]
        patronymics_m = self._data[3]
        surnames_m = self._data[4]

        names_w_r = self._data[5]
        names_w = self._data[6]
        patronymics_w_r = self._data[7]
        patronymics_w = self._data[8]
        surnames_w = self._data[9]

        if self.rare:
            names_m += names_m_r
            patronymics_m += patronymics_m_r
            names_w += names_w_r
            patronymics_w += patronymics_w_r

        self._base = {
            'man': {
                'name': self._load_set(names_m, self.name_max_len),
                'patronymic': self._load_set(patronymics_m, self.patronymic_max_len),
                'surname': self._load_set(surnames_m, self.surname_max_len),
            },
            'woman': {
                'name': self._load_set(names_w, self.name_max_len),
                'patronymic': self._load_set(patronymics_w, self.patronymic_max_len),
                'surname': self._load_set(surnames_w, self.surname_max_len),
            },
        }

    def _select_gender_distribution(self):
        dice = random.uniform(0, 1)
        gender = 0.5
        if 0 <= self.gender <= 1:
            gender = self.gender
        return dice < gender

    def _get_object(self, gender, elem_type, reduction=False):
        sub = 'man' if gender else 'woman'
        base = self._base[sub][elem_type]
        name = random.choice(base)
        if reduction:
            name = name[0] + '.'
        if self.transliterate:
            name = transliterate_word(name)
        if self.uppercase:
            name = name.upper()
        return name

    def _format_person(self, person):
        if self.output_type == 'dict':
            result = person
        elif self.output_type == 'list':
            result = list(person.values())
        elif self.output_type == 'tuple':
            result = tuple(person.values())
        elif self.output_type == 'str':
            result = ' '.join([v for k, v in person.items() if v is not None])
        else:
            raise ValueError("Output_type does not have value 'str', 'list, 'tuple' or 'dict'. ")
        return result

    def get_person(self, **kwargs):
        self._set_options(**kwargs)
        gender = self._select_gender_distribution()
        name = self._get_object(gender, 'name', self.name_reduction)
        patronymic = self._get_object(gender, 'patronymic', self.patronymic_reduction)
        surname = self._get_object(gender, 'surname', self.surname_reduction)
        person = {
            'name': name if self.name else None,
            'patronymic': patronymic if self.patronymic else None,
            'surname': surname if self.surname else None,
        }
        return self._format_person(person)

    def get_batch(self, **kwargs):
        batch = ()
        for _ in range(self.count):
            fio = self.get_person(**kwargs)
            batch += (fio, )
        return batch


__all__ = (
    'RussianNames',
)
