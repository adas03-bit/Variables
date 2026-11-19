#define arrays
#an array is a data structure that stores a collection of multiple items or values under a single name.

def getValidInteger(prompt, minimum, maximum):
    while True:
        try:
            number = int(input(prompt))
            if number <= minimum or number <= maximum:
                return number
            else:
                print("Error: Enter a number between", minimum, "and", maximum)
        except ValueError:
            print("Error: Please enter a valid whole number")
def getValidFloat(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Error: Please enter a valid number")

#MOVIE RATING SYSTEM
def inputRating():

    ratings = []
    for i in range(5):
        rating = getValidInteger("Enter a rating for"+ " movie " + str(i+1) + "(1-10): ", 1, 10)
        ratings.append(rating)
    return ratings
def displayRating(array, movieIndex):
    print("movie", movieIndex + 1, "rating:", array[movieIndex])
def calculateAverageRating(array):
    total = 0
    for rating in array:
        total += rating
    average = total / len(array)
    return average
def updateRating(array, index, newRating):
    array[index] = newRating
def movieRatingProgram():
    print("\n=====MOVIE RATING SYSTEM=====")
    ratings = inputRating()
    while True:
        print("\nMovieRating Menu")
        print("1. View a movie rating")
        print("2. Calculate average rating")
        print("3. Update a movie rating")
        print("4. Return to main menu")
        choice = getValidInteger("Choose an option (1-4): ", 1, 4)
        if choice == 1:
            movieNumber = getValidInteger("Which movie do you want to review? (1-5): ", 1, 5)
            movieIndex = movieNumber - 1
            displayRating(ratings, movieIndex)
        elif choice == 2:
            average = calculateAverageRating(ratings)
            print("Average movie rating:", round(average,2))
        elif choice == 3:
            movieNumber = getValidInteger("Which movie do you want to update? (1-5): ", 1, 5)
            newRating = getValidInteger("Enter the new rating (1-10): ", 1, 10)
            movieIndex = movieNumber - 1
            updateRating(ratings, movieIndex, newRating)
            print("Rating successfully updated!")
            displayRating(ratings, movieIndex)
        elif choice == 4:
            print("Returning to main menu...")
            break

def inputTemperatures():
    temperatures = []
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i in range(7):
        temperature = getValidFloat("Enter the temperature for " + days[i] + "(Fahrenheit): ")
        temperatures.append(temperature)
    return temperatures
def getTemperatureByDay(array, dayIndex):
    return array[dayIndex]
def calculateAverage(array):
    total = 0
    for temperature in array:
        total += temperature
        average = total / len(array)
        return average
def temperatureProgram():
    print("\n====WEEKLY TEMPERATURE TRACKER=====")
    temperatures = inputTemperatures()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    while True:
        print("\nTemperature Menu")
        print("1. Check a specfic day")
        print("2. Calculate weekly average")
        print("3. Return to main menu")
        choice = getValidInteger("Choose an option (1-3): ", 1, 3)
        if choice == 1:
            dayNumber = getValidInteger("Enter a day number (1-7): ", 1, 7)
            dayIndex = dayNumber - 1
            temperature = getTemperatureByDay(temperatures, dayIndex)
            print(days[dayIndex], "temperature:", temperature, "Fahrenheit")
        elif choice == 2:
            average = calculateAverage(temperatures)
            print("Average temperature:", (average), "Fahrenheit")
        elif choice == 3:
            print("Returning to main menu...")
            break
    #MAIN PROGRAM
def main():
    while True:
        print("\n======================")
        print("       MAIN MENU")
        print("======================")
        print("1. Movie Rating System")
        print("2. Weekly Temperature Tracker")
        print("3. Exit.")
        choice = getValidInteger("Choose an option (1-3): ", 1, 3)
        if choice == 1:
            movieRatingProgram()
        elif choice == 2:
            temperatureProgram()
        elif choice == 3:
            print("Thank you for using this program!")
            break
if __name__ == "__main__":
    main()

