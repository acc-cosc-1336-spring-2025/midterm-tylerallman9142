#add import

import question_c
from question_c import get_bonus_pay_amount

def main():
    result = question_c.get_bonus_pay_amount(1200)
    try:
        sales = float(input("Enter sales amount: "))
        print("Bonus pay amount:", get_bonus_pay_amount(sales))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

main()