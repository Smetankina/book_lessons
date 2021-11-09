class BankAccount:

    def __init__(self, name, balance):

        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance

    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    my_balance = property(get_balance)
    my_balance = my_balance.getter(set_balance)
    my_balance = my_balance.getter(delete_balance)

