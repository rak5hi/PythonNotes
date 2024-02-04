####################################################

def cube(x):
    return x*x*x

y = lambda x: x*x*x

print('using normal func: ', cube(5))
print('using lambda func: ', y(5))
####################################################

def square(a: float) -> float:
    return a ** 2

sq = lambda a: a ** 2

print(square(4))
print(sq(4))

####################################################

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7]

even: list[int] = list(filter(lambda a: a % 2 == 0, numbers))

print(even)

####################################################

func = lambda text, n: print(text * n)

func('Hello', 2)