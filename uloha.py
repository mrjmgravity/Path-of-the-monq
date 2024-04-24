import random


def time(seconds):
    hours = seconds//3600
    minutes = (seconds % 3600)//60
    seconds = seconds % 60
    print("H:", hours, "M:", minutes,"S:", seconds)


# time(3200)


def postupnost(parameter):
    a = 0
    b = 1
    c = a + b
    for i in range(parameter):
        print(a)
        a = b
        b = c
        c = a + b


# postupnost(9)


def throw():
    return random.randint(1, 6)


def while_even():
    sum = 0
    num = throw()
    sum += num
    print(num)
    while num % 2 != 0:
        num = throw()
        sum += num
        print(num)

    return sum


print(while_even())
