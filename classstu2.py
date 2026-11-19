class Student:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
    def get_name(self):
        return self.name
    def calculateAverage(self):
        return (self.score1 + self.score2 + self.score3) / 3
    def getLetter(self):
        average = self.calculateAverage()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"



def main() :
    try:

        name=input("Enter students name: ")
        score1=int(input("Enter first score: "))
        score2=int(input("Enter second score: "))
        score3=int(input("Enter third score: "))

        student = Student(name, score1, score2, score3)

        if not all (0<=score<=100 for score in [student.score1,student.score2, student.score3]):
            print("Error: scores must be between 0 and 100")
            return

        print("\nStudent Name:", student.name)
        print("Average:", f"{student.calculateAverage():.2f}")
        #print("Circle area:", f"{circle.calculate_area():.2f}")
        print("Letter Grade:", student.getLetter())
    except ValueError:
        print("Error: Please enter valid numbers for test scores.")


if __name__ == '__main__':
    main()



