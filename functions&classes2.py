import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return math.pi*self.radius**2
class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def calculate_area(self):
        return self.height*self.width
def main():
    while True:
        print("\nArea Calculator")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Exit")
        choice=input("Choose an option: ")
        try:
            if choice=="1":
                radius=float(input("Enter the radius: "))
                if radius < 0:
                    print("Error: Radius cannot be negative")
                    continue
                circle=Circle(radius)
                print("Circle area:",f"{circle.calculate_area():.2f}")
            elif choice=="2":
                length=float(input("Enter the length: "))
                width=float(input("Enter the width: "))
                if length < 0 or width < 0:
                    print("Error: measurements cannot be negative")
                    continue
                rectangle=Rectangle(length,width)
                print("Rectangle area:",f"{rectangle.calculate_area():.2f}")
            elif choice=="3":
                print("Goodbye")
                break
            else:
                print("Invalid input, please choose 1,2,3.")
        except ValueError:
            print("Error: Please enter valid numbers.")


main()

