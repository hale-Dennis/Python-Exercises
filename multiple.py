
def is_multiple(n, m):
    if n == 0:
        return False
    if n % m == 0:
        return True 
    return False

if is_multiple(9,3):
    print("6 is a multiple of 3")
else:
    print("Not a multiple")