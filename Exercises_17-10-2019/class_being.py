class Mixin(object):
    def __init__(self):
        self.name = object.name

    def move(self):
        print(f'{self.name} is moving')

    def close_eyes(self):
        print(f'{self.name} has closed eyes')


class Being:
    def __init__(self, name):
        self.name = name


class Cat(Being, Mixin):
    def __init__(self, name):
        super(Cat, self).__init__(name)


class Dog(Being, Mixin):
    def __init__(self, name):
        super(Dog, self).__init__(name)


class Bird(Being, Mixin):
    def __init__(self, name):
        super(Bird, self).__init__(name)


cat = Cat('Jake')
cat.move()
cat.close_eyes()

dog = Dog('Doggy')
dog.move()
dog.close_eyes()
