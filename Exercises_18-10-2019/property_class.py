PROGR_LANGS = [
    'C++',
    'C#',
    'Python',
    'Java'
]


class Programmer:

    def __init__(self, name, lang):
        self._name = name
        for language in lang.split(' '):
            if language not in PROGR_LANGS:
                raise ValueError(f'{language} language doesn\'t exist')
        self._lang = lang

    @property
    def name(self):
        return self._name

    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, lang):
        print(lang.split(' '))
        for language in lang.split(' '):
            if language not in PROGR_LANGS:
                raise ValueError(f'{language} language doesn\'t exist')
        self._lang = lang
        print(f'{self.name} changed his lang to {self._lang}')

    @name.setter
    def name(self, name):
        self._name = name


if __name__ == '__main__':
    Sundwell = Programmer('Sundwell', 'Python C++')
    Sundwell.lang += ' C#'
