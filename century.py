import math

def checkCentury(year):
    return math.ceil(year / 100)


century = checkCentury(1900)

print(century)