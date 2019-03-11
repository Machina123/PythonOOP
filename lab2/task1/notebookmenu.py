from notebook import Note, Notebook
import sys

class Menu:
    
    def __init__(self):
        self.notebook = Notebook()
        self.options = {"1": self.show_notes, "2": self.search_notes, "3": self.add_note, "4": self.modify_note, "5": self.quitme}

    def show_notes(self, filter=False, filter_text=None):
        if filter:
            if isinstance(filter_text, str):
                for note in self.notebook.search(filter_text):
                    print(note)
            else:
                raise AttributeError("filter_text is not of type str")
        else:
            for note in self.notebook.notes:
                print(note)
    
    def search_notes(self):
        needle = input("Podaj szukany tekst: ")
        self.show_notes(filter = True, filter_text = needle)
    
    def add_note(self):
        tag = input("Tag notatki: ")
        text = input("Tekst notatki: ")
        new_note = Note(text, tag)
        self.notebook.new_note(new_note)

    def modify_note(self):
        note_id = int(input("ID notatki do zmiany: "))
        new_tag = input("Nowy tag: ")
        new_text = input("Nowa treść: ")
        self.notebook.modify_tag(note_id, new_tag)
        self.notebook.modify_text(note_id, new_text)
    
    def run(self, option):
        self.options[option]()
    
    def quitme(self):
        sys.exit()
    
    def show_menu(self):
        menu_text = "--- Menu ---\n1. Pokaż notatki\n2. Przeszukaj notatki\n3. Dodaj notatkę\n4. Zmodyfikuj notatkę\n5. Wyjście"
        print(menu_text)

if __name__ == "__main__":
    menu = Menu()
    while True:
        menu.show_menu()
        option = input("Wybrana opcja? ")
        if not option in menu.options:
            print("Nieprawidłowa opcja\n")
        else:
            menu.run(option)
    