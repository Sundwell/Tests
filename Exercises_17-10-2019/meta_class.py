class MyMetaClass(type):

    def __new__(mcs, cls_name, cls_parents, cls_attrs):
        count = 0
        for name, value in cls_attrs.items():
            if (name.startswith('__') and name.endswith('__') and count > 3) or name == '__repr__':
                raise AttributeError
            else:
                count += 1

        return type.__new__(mcs, cls_name, cls_parents, cls_attrs)


class Foo(metaclass=MyMetaClass):

    __my_name__ = "Foo"

    def __init__(self):
        self.name = self.__my_name__

    # def __del__(self):
    #     print('Foo deleted.')

    def print_hi(self):
        print(f'Hello, I am {self.name}, and my len is {self.name.__len__()}')

    # def __repr__(self):
    #     print('Im repr')


if __name__ == '__main__':
    foo = Foo()
    print(foo.name)
    foo.print_hi()
