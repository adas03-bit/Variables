while True:
    try:
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the second number: "))
        total=num1+num2
        if total > 0:
            print("The sum is positive", total)
        elif total < 0:
            print("The sum is negative", total)
        else:
            print("The sum is zero",total)

    except ValueError:
            print ("Please enter a numeric value")

    again = input("Would you like to enter 2 more numbers?")
    if again.lower() != "yes":
            print ("program ended.")
            break


while True:
    try:
        age=int(input("Enter your age: "))

        if age < 0:
            print ("Error: Age cannot be negative.")
            continue
        if age > 130:
            print ("Error: Age cannot be greater than 130.")
            continue
        if age <= 12:
            print ("Category: Child")
        elif age <= 19:
            print ("Category: Teen")
        elif age <= 64:
            print ("Category: Adult")
        else:
            print ("Category: Senior")
    except ValueError:
            print("Please enter a valid number")

    again = input("Would you like to enter other ages? ")
    if again.lower() != "yes":
            print ("program ended.")
            break

