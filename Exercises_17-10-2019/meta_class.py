class MyMetaClass(type):

    def __new__(mcs, cls_name, cls_parents, cls_attrs):
        rejected_methods = ['__contains__', '__format__', '__len__', '__repr__']
        for name, value in cls_attrs.items():
            # print(name)
            if (name.startswith('__') and name.endswith('__')) and name in rejected_methods:
                raise AttributeError

        return type.__new__(mcs, cls_name, cls_parents, cls_attrs)


class Foo(metaclass=MyMetaClass):

    age = 5

    def __init__(self):
        self.name = 'Foo'

    def print_hi(self):
        print(f'Hello, I am {self.name}')

    # def __repr__(self):
    #     print('Im repr')
    # Если расскоментить две верхние строчки то будет AttributeError


if __name__ == '__main__':
    foo = Foo()
    print(foo.name)
    foo.print_hi()

