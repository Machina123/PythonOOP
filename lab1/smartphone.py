import pickle

class Smartphone:

    def __init__(self, manufacturer, model, price):
        """Konstruktor klasy Smartphone"""
        self._manufacturer = manufacturer
        self._model = model
        self._price = price

    def get_manufacturer(self):
        """Pobieranie producenta"""
        return self._manufacturer

    def set_manufacturer(self, newmfg):
        """Ustawianie producenta"""
        self._manufacturer = newmfg

    def get_model(self):
        """Pobieranie modelu"""
        return self._model

    def set_model(self, newmdl):
        """Ustawianie modelu"""
        self._model = newmdl

    def get_price(self):
        """Pobieranie ceny"""
        return self._price

    def set_price(self, newprc):
        """Ustawianie ceny"""
        self._price = newprc

if __name__ == '__main__':
    list_sp = []
    galaxy = Smartphone("Samsung", "Galaxy S10", 3999)
    apple = Smartphone("Apple", "iPhone XS", 4299)
    the_better_one = Smartphone("Xiaomi", "Mi 8", 2299)
    list_sp.append(galaxy)
    list_sp.append(apple)
    list_sp.append(the_better_one)

    print("Lista przed peklowaniem:")
    for i in range(len(list_sp)):
        print(f"Smartfon #{i+1}: {list_sp[i].get_manufacturer()} {list_sp[i].get_model()}, cena: {list_sp[i].get_price()}")

    phone_file = open("phones.dat", "wb")
    pickle.dump(list_sp, phone_file, protocol=pickle.HIGHEST_PROTOCOL)
    phone_file.close()

    phone_file = open("phones.dat", "rb")
    list_sp_unp = pickle.load(phone_file)
    phone_file.close()

    print("Lista po odpeklowaniu:")
    for i in range(len(list_sp_unp)):
        print(f"Smartfon #{i+1}: {list_sp_unp[i].get_manufacturer()} {list_sp_unp[i].get_model()}, cena: {list_sp_unp[i].get_price()}")
