# 1


def print_count():
    print(f'Count of inherits = {Useless.count_of_inherits}')


class Useless:
    count_of_inherits = 0


class First(Useless):
    Useless.count_of_inherits += 1


class Second(Useless):
    Useless.count_of_inherits += 1


print_count()
