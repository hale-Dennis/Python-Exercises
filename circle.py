

def calc_cirle(radius):
    area = round(float(22 / 7 * radius ** 2), 2)
    diameter = float(radius * 2)
    circumference = round(float(2 * 22 / 7 * radius), 2)
    return {"area":area, "diameter": diameter, "circumference": circumference}


radius = float(input("Enter the radius of the circle: "))
result = calc_cirle(radius)

print("area ==>", result["area"], "\ndiameter ==>", result["diameter"], "\ncircumference ==>", result["circumference"])
