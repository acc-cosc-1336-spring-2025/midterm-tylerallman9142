#add import

import question_d
from question_d import get_day_of_week

def main():
    result = question_d.get_day_of_week("day")
    while True:
        try:
            user_input = input("Enter a number (1-7) to get the day of the week, or 'q' to quit: ")
            if user_input.lower() == 'q':
                break
            day_number = int(user_input)
            print("Day of the week:", get_day_of_week(day_number))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")

main()