# Autor: Patryk Ciepiela
class RocketEngine:
    count = 0
    all_power = 0

    def __init__(self, name, power, working=False):
        """Konstruktor klasy RocketEngine"""
        self._name = name
        self._power = power
        self._working = working
        RocketEngine.count += 1

    def start(self):
        """ Uruchamianie silnika """
        if not self._working:
            RocketEngine.all_power += self._power
            self._working = True

    def stop(self):
        """Zatrzymanie silnika"""
        if self._working:
            RocketEngine.all_power -= self._power
            self._working = False

    def __str__(self):
        """Raport o silniku"""
        working_condition = "Tak" if self._working else "Nie"
        return f"Silnik \"{self._name}\": Moc = {self._power}; Pracuje? {working_condition}"

    def __del__(self):
        """Dematerializacja silnika"""
        RocketEngine.count -= 1

    @staticmethod
    def status():
        """Raport o dostępnych silnikach i ich mocy"""
        print(f"Ilość silników: {RocketEngine.count}, Łączna aktywna moc: {RocketEngine.all_power}")

def engines_status(list_engines):
    """Metoda pomocnicza - raport ogólny o stanie silników"""
    RocketEngine.status()
    for i in range(len(list_engines)):
        print(list_engines[i])

if __name__ == '__main__':
    list_engines = []
    mnvr_eng1 = RocketEngine("Silnik manewrowy lewy", 50)
    list_engines.append(mnvr_eng1)
    mnvr_eng2 = RocketEngine("Silnik manewrowy prawy", 50)
    list_engines.append(mnvr_eng2)
    print("Manewrowanie...")
    mnvr_eng1.start()
    mnvr_eng2.start()
    engines_status(list_engines)
    print("\nRozpędzanie do hiperprędkości...")
    warmup_eng1 = RocketEngine("Silnik rozpędzający lewy", 500)
    warmup_eng2 = RocketEngine("Silnik rozpędzający prawy", 500)
    list_engines.append(warmup_eng1)
    list_engines.append(warmup_eng2)
    mnvr_eng2.stop()
    mnvr_eng1.stop()
    warmup_eng1.start()
    warmup_eng2.start()
    engines_status(list_engines)
    print("\nHiperprędkość")
    hyper_eng1 = RocketEngine("Hipersilnik lewy", 400000)
    hyper_eng2 = RocketEngine("Hipersilnik prawy", 400000)
    list_engines.append(hyper_eng1)
    list_engines.append(hyper_eng2)
    hyper_eng1.start()
    hyper_eng2.start()
    warmup_eng1.stop()
    warmup_eng2.stop()
    engines_status(list_engines)
    print("\nWyjście z hiperprędkości, manewrowanie...")
    hyper_eng1.stop()
    hyper_eng2.stop()
    list_engines.remove(hyper_eng1)
    list_engines.remove(hyper_eng2)
    list_engines.remove(warmup_eng1)
    list_engines.remove(warmup_eng2)
    del hyper_eng1
    del hyper_eng2
    del warmup_eng1
    del warmup_eng2
    mnvr_eng1.start()
    mnvr_eng2.start()
    engines_status(list_engines)
    print("\nCumowanie w porcie")
    mnvr_eng2.stop()
    mnvr_eng1.stop()
    engines_status(list_engines)
