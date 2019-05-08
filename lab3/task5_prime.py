import math
def primes():
    number = 3
    yield 2
    while True:
        for x in range(2, int(math.sqrt(number)+1)):
            if number % x == 0:
                break
        else:
            yield number
        number += 1

with open("l3_t5_primes.txt", "w") as f:
    count = 1;
    for num in primes():
        if count > 10000:
            break
        f.write(f"{num}\n")
        count += 1
