my_dict = {}


def decorator(func):
    def wrapper(name, points):
        my_dict.update(func(name, points))
        return my_dict
    return wrapper


@decorator
def print_some(name, points):
    return {name: points % 100}


if __name__ == "__main__":
    print_some("Soren", 210)
    print_some("Andrew", 53)
    print_some("Sarah", 76)
    print_some("Maxwell", 58)
    print(my_dict)
