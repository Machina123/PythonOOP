class Account:

    def __init__(self, balance):
        """ Konstruktor w klasie Account - tworzenie nowego konta """
        self._balance = balance

    def pay(self, amount):
        """ Wpłata na konto """
        self._balance += amount

    def take(self, amount):
        """ Wypłata z konta """
        if self._balance - amount < 0:
            print("Niewystarczające środki na wykonanie tej transakcji!")
        else:
            self._balance -= amount

    def show_balance(self):
        """ Zwraca dostępne środki na koncie """
        return self._balance

    def __str__(self):
        """ Tekstowa reprezentacja obiektu """
        return f"Dostępne środki: {round(self.show_balance(), 2)}"

if __name__ == '__main__':
    print("Operacja: założenie konta, środki początkowe = 500")
    acct = Account(500)
    print(f"\t{acct}")
    print("Operacja: wpłata 300")
    acct.pay(300)
    print(f"\t{acct}")
    print("Operacja: wypłata 800.01")
    acct.take(800.01)
    print(f"\t{acct}")
    print("Operacja: wypłata 799.99")
    acct.take(799.99)
    print(f"\t{acct}")
