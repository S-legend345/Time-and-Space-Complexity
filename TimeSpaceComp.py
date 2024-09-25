def summation(n):
    sum = n*(n+1)/2
    print(sum)

summation(1)
summation(2)
summation(3)
summation(4)
summation(5)


def add(n):
    summ = 0
    for i in range(1,n+1):
        summ += i
    print(summ)

add(15)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True

def first_prime_num(n):
    primes = []
    num = 2
    while len(primes) < 10:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

print(first_prime_num(12))


def squares(a):
    for i in range(1, a+1):
        print(i**2)

squares(10)
