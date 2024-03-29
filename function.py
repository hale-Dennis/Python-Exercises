#exercise one 
'''
def calculate_area(base =0, height=0, length=0, width=0, shape="triangle"):
    if shape == "triangle":
        return 0.5 * base * height
    elif shape == "rectangle":
        return length * width

shape = input("shape type?:")
if shape == "triangle":
    b= float(input("Enter base of triangle:"))
    h = float(input("Enter height of triangle:"))
    area = calculate_area(base=b, height=h)
    print("Area of triangle is", area)
elif shape == "rectangle":
    l = float(input("Enter length of rectangle:"))
    w = float(input("Enter width of rectangle:"))
    area = calculate_area(length=l, width=w,shape=shape)
    print("Area of rectangle is", area)
else: 
    print("Invalid shape")
'''

#exercise two
def pattern(lines):
    for i in range(1,lines+1):
        s = ''
        for j in range(i):
            s += '*'
        print(s)
   

print(pattern(3))



