#exercise one
integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

binary_dict = {i:b for i,b in zip(integer, binary)}


#exercise two
integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [i*(-1) for i in integer]

#exercise three
integer = [1, -1, 2, -2, 3, -3]
sql = {i**2 for i in integer}