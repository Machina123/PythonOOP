import itertools

class Fibonacci:
    def __init__(self, stop):
        self._a = 0
        self._b = 1
        self._stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        fibo = self._a
        if fibo > self._stop:
            raise StopIteration()
        else:
            self._a, self._b = self._b, self._a + self._b
            return fibo

for i in Fibonacci(100):
    print(i)

def gen_fibo(stop):
    a = 0
    b = 1
    while a < stop:
        yield a
        a, b = b, a+b

for j in gen_fibo(100):
    print(j)


def gen_fibo_inf():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


gen = itertools.islice(gen_fibo_inf(), 100000, 100020)
with open("l3_t3_liczby.txt", "w") as f:
    first = True
    for i in gen:
        f.write(f"{i}\n")
        if first:
            print(f"Ilość cyfr dla F_100000: {len(str(i))}")
            first=False
