

def fib():
    a = 0
    b = 1
    while True:
        yield a
        a = b
        b = a + b

for number in fib():
    if number > 20: 
        break
    else:
        print(number)


def square_sequence():
    i = 1
    while True:
        yield i**2
        i += 1

        
gen = square_sequence()
next(gen)