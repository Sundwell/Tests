my_dict = {}


def decorator(func):
    def wrapper(name, points):
        print(f'args are: {name}, {points}')
        result = func(name, points)
        return result
    return wrapper


def print_some(name, points):
    my_dict.update({name: points})
    return my_dict


decorated_print_some = decorator(print_some)
decorated_print_some("Soren", 100)
decorated_print_some("Andrew", 53)
decorated_print_some("Sarah", 76)
decorated_print_some("Maxwell", 58)
print(my_dict)
