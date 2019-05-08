class Pupil:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.marks = {}

    @property
    def name(self):
        return self.__dict__["name"]

    @name.setter
    def name(self, val):
        while len(val) <  3 or not val.isalpha():
            val = input("Nieprawidlowe dane. Imie? ")
        self.__dict__["name"] = val

    @property
    def surname(self):
        return self.__dict__["surname"]

    @surname.setter
    def name(self, val):
        while len(val) < 3 or not val.isalpha():
            val = input("Nieprawidlowe dane. Nazwisko? ")
        self.__dict__["surname"] = val

    def complete_marks(self):
        marks = {"1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5", "5.5", "6"}
        marks = [float(s) for s in marks]
        while True:
            course = input("Przedmiot? ")
            while len(course) < 3 or not course.isalpha() or course in self.marks:
                course = input("Niepoprawne dane. Przedmiot? ")
            grade = float(input("Ocena? "))
            while grade not in marks:
                grade = float(input("Nieprawidlowe dane. Ocena? "))
            self.marks[course] = float(grade)

            end = input("Aby zakonczyc wpisz x")
            if end == "x":
                break

    def show_marks(self):
        print(self.marks)

    def mean(self):
        sumgrades = 0.0
        for grade in self.marks.values():
            sumgrades += grade
        return sumgrades / len(self.marks)

    def __str__(self):
        return f"Imie: {self.name}, Nazwisko: {self.surname}, Srednia: {self.mean()}"

class Student(Pupil):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.weights = []

    def complete_weights(self):
        for k in self.marks:
            weight = float(input(f"Waga dla kursu {k}? "))
            while not 0 <= weight <= 1:
                weight = float(input(f"Waga dla kursu {k}? "))
            self.weights[k] = weight

    def mean(self):
        mean = 0.0
        weightsum = 0.0
        for k,v in self.marks.items():
            mean += v * self.weights[k]
            weightsum += self.weights[k]
        return mean / weightsum

    