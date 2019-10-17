def print_call():
    print(f'Class has been called {Apple.count} times')


class Apple:
    count = 0

    def __init__(self):
        Apple.count += 1
        print('New apple!')


green_apple = Apple()
red_apple = Apple()
print_call()
