def factors(number):
    fac = [1]
    for i in range(2, number+1):
        if number % i == 0:
            fac.append(i)
    return len(fac)


def primestill(num):
    primes = []
    for i in range(2, num+1):
        if factors(i) == 2:
            primes.append(i)
    print(primes)


primestill(11)