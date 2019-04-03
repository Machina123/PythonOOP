import authorization_system as auth
import sys

class Editor:

    def __init__(self):
        self.username = None
        self.options = {"a": self.login, "b": self.test, "c": self.change, "d": self.quitme}

    def login(self):
        login = input("Login: ")
        passwd = input("Haslo: ")
        try:
            auth.authenticator.login(login, passwd)
            self.username = login
        except auth.IncorrectUsername:
            print("Nieprawidlowa nazwa uzytkownika")
        except auth.IncorrectPassword:
            print("Nieprawidlowe haslo")

    def is_permitted(self, permission):
        try:
            return auth.authorizator.check_permission(self.username, permission)
        except auth.NotLoggedError:
            print("Uzytkownik nie jest zalogowany")
            return False
        except auth.NotPermittedError:
            print("Niewystarczajace uprawnienia")
            return False
        except auth.PermissionError:
            print("Nieznane uprawnienie")
            return False

    def test(self):
        if self.is_permitted("test"):
            print("Testowanie w toku...")

    def change(self):
        if self.is_permitted("change"):
            print("Wprowadzanie zmian...")

    def quitme(self):
        sys.exit()

    def run(self):
        print(f"--- MENU ---\nCo chcesz zrobic?\na. Zaloguj sie\nb. Testuj\nc. Wprowadz zmiany\nd. Wyjscie\n")
        option = input("[a/b/c/d]? ").lower()
        if not option in self.options:
            print(f"Nieprawidlowa opcja!\n\n")
        else:
            self.options[option]()

if __name__ == '__main__':
    editor = Editor()
    while True:
        editor.run()