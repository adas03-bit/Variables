class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        if num2==0:
            return "cannot divide by zero"
        return num1 / num2
    def main(self):

        calculator=Calculator()
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        print("Addition: ", calculator.add(num1, num2))
        print("Subtraction: ", calculator.subtract(num1, num2))
        print("Multiplication: ", calculator.multiply(num1, num2))
        print("Division: ", calculator.divide(num1, num2))
        while True:
            print("\nCalculator")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            choice=input("Choose an option: ")
            try:
                calculator=Calculator()
                if choice=="1":
                    num1 = int(input("Enter first number: "))
                    num2 = int(input("Enter second number: "))
                    print("Addition: ", calculator.add(num1, num2))
                    #print("Circle area:",f"{circle.calculate_area():.2f}")
                elif choice=="2":
                    num1 = int(input("Enter first number: "))
                    num2 = int(input("Enter second number: "))
                    print("Subtraction: ", calculator.subtract(num1, num2))

                elif choice=="3":
                    num1 = int(input("Enter first number: "))
                    num2 = int(input("Enter second number: "))
                    print("Multiplication: ", calculator.multiply(num1, num2))

                   
                elif choice=="4":
                    num1 = int(input("Enter first number: "))
                    num2 = int(input("Enter second number: "))
                    print("Division: ", calculator.divide(num1, num2))
                elif choice=="5":
                    print("Goodbye")
                    break
                else:
                    print("Invalid input, please choose 1,2,3.")
            except ValueError:
                print("Error: Please enter valid numbers.")



    main()

