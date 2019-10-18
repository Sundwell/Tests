import datetime


class CountError(Exception):
    pass
    # def __init__(self, message):
    #     self.message = message


class Product:

    id = [0]
    is_spoiled = False
    count = 0
    prod_name = 'NoName'

    def __init__(self, prod_name, count, date_of_expire):
        self.set_prod_name(prod_name)
        self.date_of_expire = date_of_expire
        self.id = Product.id[-1]
        Product.id.append(Product.id[-1] + 1)
        self.set_count(count)

    def check_condition(self):
        if self.date_of_expire >= datetime.datetime.today().strftime("%d-%m-%Y"):
            self.is_spoiled = True
            print(f'{self.prod_name} is spoiled.')
        else:
            self.is_spoiled = False
            print(f'{self.prod_name} is in good condition')

    def set_prod_name(self, prod_name):
        if prod_name:
            self.prod_name = prod_name
        else:
            raise NameError("Wrong name of product")

    def set_count(self, count):
        if count >= 0:
            self.count = count
        else:
            raise CountError('Count cannot be lesser than 0')


if __name__ == '__main__':
    apple = Product('apple', 2, '20-10-2019')
    orange = Product('orange', -1, '20-10-2019')
