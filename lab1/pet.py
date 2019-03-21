class Pet:
    def __init__(self, name, hunger=0, tiredness=0):
        self.name = name
        self.hunger = hunger
        self.tiredness = tiredness

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        while True:
            if isinstance(name, str) and name.isalpha() and len(name) >= 3:
                self._name = name
                break
            else:
                print("Niepoprawne imię zwierzaka")
                name = input("Podaj nowe imię dla zwierzaka: ")

    @property
    def mood(self):
        happiness = self.hunger + self.tiredness
        if happiness <= 5:
            return "szczęśliwy"
        elif 5 <= happiness <= 10:
            return "zadowolony"
        elif 11 <= happiness <= 15:
            return "poddenerwowany"
        else:
            return "wściekły"

    def talk(self):
        print(f"Mam na imię {self.name} i jestem {self.mood}")

    def eat(self, food=4):
        self._passage_of_time()
        if (self.hunger - food  < 0):
            self.hunger = 0
        else:
            self.hunger -= food;

    def play(self, fun=4):
        self._passage_of_time()
        if(self.tiredness - fun < 0):
            self.tiredness = 0
        else:
            self.tiredness -= fun

    def __str__(self):
        return f"{self.name}, głód: {self.hunger}, zmęczenie: {self.tiredness}, humor: {self.mood}"

if __name__ == '__main__':
    print("--- Menu ---")
    name=input("Podaj imię zwierzaka: ")
    pet = Pet(name);
    print(f"Zwierzak o imieniu {name} narodził się")

    while True:
        try:
            choice = int(input(
                f"Co chcesz zrobić?\n"
                f"1. Nakarm zwierzaka (głód: {pet.hunger})\n"
                f"2. Pobaw się ze zwierzakiem (znudzenie: {pet.tiredness})\n"
                f"3. Informacja o nastroju zwierzaka\n"
                f"4. Informacja o parametrach życiowych\n"
                f"5. Uśpij zwierzaka (awwwww :( )\n"
                f"1/2/3/4/5? "
            ))
        except ValueError:
            print("Niewłaściwy wybór!")
            continue
        else:
            if choice == 1:
                try:
                    pet.eat(food=int(input("Ile jedzenia? ")))
                except ValueError:
                    pet.eat()
                    continue
                finally:
                    print(pet.hunger)
            elif choice == 2:
                try:
                    pet.play(fun=int(input("Czas zabawy? ")))
                except ValueError:
                    pet.play()
                    continue
                finally:
                    print(pet.hunger)
            elif choice==3:
                pet.talk()
            elif choice==4:
                print(pet)
            elif choice==5:
                break
            else:
                print("Nieprawidłowa opcja!")
                continue
