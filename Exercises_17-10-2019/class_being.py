class MixinMovements:
    name = None

    def move_right(self):
        print(f'{self.__class__.__name__} {self.name} moved right')

    def move_left(self):
        print(f'{self.__class__.__name__} {self.name} moved left')

    def jump(self):
        print(f'{self.__class__.__name__} {self.name} jumped')

    def lay_down(self):
        print(f'{self.__class__.__name__} {self.name} laid down')


class MixinEyes:
    name = None

    def close_eyes(self):
        print(f'{self.__class__.__name__} {self.name} closed eyes')

    def open_eyes(self):
        print(f'{self.__class__.__name__} {self.name} opened eyes')

    def focus_on_you(self):
        print(f'{self.__class__.__name__} {self.name} is looking on you')


class MixinLegs:
    name = None

    def step_by_right_leg(self):
        print(f'{self.__class__.__name__} {self.name} did step by right leg')

    def step_by_left_leg(self):
        print(f'{self.__class__.__name__} {self.name} did step by left leg')


class MixinHands:
    name = None

    def raise_hands(self):
        print(f'{self.__class__.__name__} {self.name} raised hands')

    def lower_hands(self):
        print(f'{self.__class__.__name__} {self.name} lowered hands')

    def wave(self):
        print(f'{self.__class__.__name__} {self.name} waved you')


class MixinHead:
    name = None

    def head_up(self):
        print(f'{self.__class__.__name__} {self.name} upped head')

    def head_shake(self):
        print(f'{self.__class__.__name__} {self.name} shook head')


class Being:
    def __init__(self, name):
        self.name = name


class Cat(MixinMovements, MixinEyes, MixinHead, MixinLegs, Being):
    pass


class Dog(MixinMovements, MixinEyes, MixinHead, MixinLegs, Being):
    pass


class Monkey(MixinMovements, MixinEyes, MixinHands, MixinHead, MixinLegs, Being):
    pass


cat = Cat('Jake')
cat.move_right()
cat.step_by_left_leg()
cat.step_by_right_leg()
cat.lay_down()

dog = Dog('Andrew')
dog.jump()
dog.close_eyes()
dog.head_shake()
dog.open_eyes()

monkey = Monkey('Maxwell')
monkey.raise_hands()
monkey.close_eyes()
monkey.open_eyes()
monkey.wave()
