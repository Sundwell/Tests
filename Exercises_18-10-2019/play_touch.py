import random
import time


def check_winner(obj1, obj2, end=False):
    if abs(obj1.touches - obj2.touches) > 2 or end:
        print('\nThe game is OVER!!!')
        if obj1.touches > obj2.touches:
            print(f'The Winner is {obj1.name}!!!')
        elif obj1.touches < obj2.touches:
            print(f'The Winner is {obj2.name}!!!')
        exit()


class Wall:
    def __init__(self, name='None'):
        if not name.endswith('wall'):
            self.name = 'simple wall'
        else:
            self.name = name

    def touch(self, obj):
        print(f'{obj.name} touched the {self.name}!')
        return 1


class Character:

    def __init__(self, name):
        self.name = name
        self.touches = 0

    def touch_wall(self, obj):
        self.touches += obj.touch(self)


if __name__ == '__main__':
    char1 = Character('Sundwell')
    char2 = Character('Andrew')
    total_touches = 0
    simple_wall = Wall()
    while True:
        if random.randint(1, 2) == 1:
            char1.touch_wall(simple_wall)
            total_touches += 1
        else:
            char2.touch_wall(simple_wall)
            total_touches += 1
        check_winner(char1, char2)
        if total_touches % 10 == 0:
            print(f'\n!!!WOW!!! There are already {total_touches} touches!!!\n')
        time.sleep(0.5)
        if total_touches > 10:
            print("\nThe game is taking too much time. Game is ending.")
            check_winner(char1, char2, end=True)
