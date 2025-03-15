#write functions here, don't add input('') statements here!

def get_bonus_pay_amount(sales):
    if sales < 0 or sales > 1999:
        return "Invalid Arguments"
    elif 0 <= sales <= 499:
        return sales * 0.05
    elif 500 <= sales <= 999:
        return sales * 0.06
    elif 1000 <= sales <= 1499:
        return sales * 0.07
    elif 1500 <= sales <= 1999:
        return sales * 0.08