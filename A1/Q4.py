# 4. Calculate area and perimeter of a rectangle
def rectangle_area_perimeter():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    area = length * width
    perimeter = 2 * (length + width)
    
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")

rectangle_area_perimeter()