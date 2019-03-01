import random

class Coin:

    def __init__(self):
        self._side = "Heads" if random.randrange(2)==0 else "Tails"


    def throw(self):
        self._side = "Heads" if random.randrange(2)==0 else "Tails"


    def show_side(self):
        return self._side


def test_class():
    coin1 = Coin()
    coin2 = Coin()
    coin3 = Coin()
    print("Throwing all coins")
    coin1.throw()
    coin2.throw()
    coin3.throw()
    print(f"Coin 1: {coin1.show_side()}")
    print(f"Coin 2: {coin2.show_side()}")
    print(f"Coin 3: {coin3.show_side()}")

# test_class()