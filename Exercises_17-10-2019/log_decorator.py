my_dict = {}


def decorator(func):
    def wrapper(name, points):
        print(f'args are: {name}, {points}')
        result = func(name, points)
        return result
    return wrapper


@decorator
def print_some(name, points):
    my_dict.update({name: points})
    return my_dict


if __name__ == "__main__":
    print_some("Soren", 100)
    print_some("Andrew", 53)
    print_some("Sarah", 76)
    print_some("Maxwell", 58)
    print(my_dict)
