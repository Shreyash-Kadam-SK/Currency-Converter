currency_list = {'Rupees': 10.00, 'Dollar': 0.12}


def input_currency(user_choiceint):
    if user_choiceint in currency_list:
        user_amt = int(input("enter the amount you want to convert: "))
        img_value = user_amt / currency_list[user_choiceint]
        return img_value
    else:
        print(f"Currency '{user_choiceint}' not found in the list.")


def output_currency(user_choiceout, img_value):
    if user_choiceout in currency_list:
        output_value = img_value * currency_list[user_choiceout]
        print(output_value)
    else:
        print(f"Currency '{user_choiceout}' not found in the list.")

#main_function
for currency in currency_list:
    print(currency)
img_result = input_currency(input("Enter your currency you want to input: "))
for currency in currency_list:
    print(currency)
output_currency(input("Enter the currency for the output value: "), img_result)