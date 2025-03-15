#add import

import question_b

def main():
    result = question_b.get_fahrenheit(5)

    print("Celsius to Fahrenheit Conversion Table")
    print("Celsius | Fahrenheit")
    print("--------------------")
    for celsius in range(21):
        print(f"{celsius:7} | {question_b.get_fahrenheit(celsius):10.1f}")

main()