currency_dict = {'Rupees': 10.00, 'Dollar': 0.12, 'BTC': 0.0000019, 'CAD': 0.16, 'NZD': 0.20, 'EGP': 5.73, 'AED': 0.44,
                 'AUD': 0.18}
currencies = ['Rupees', 'Dollar', 'BTC', 'CAD', 'NZD', 'EGP', 'AED', 'AUD']
currenciesoutput_list = []


def input_currency():
    while True:
        user_choiceinput = input("Enter your currency you want to input: ")
        if user_choiceinput in currency_dict:
            while True:
                user_amt = input("enter the amount you want to convert: ")
                if user_amt.isdigit():
                    ua = int(user_amt)
                    img_value = ua / currency_dict[user_choiceinput]
                    break
                else:
                    print("Enter a valid Integer")
            for i in range(len(currencies)):
                if user_choiceinput != currencies[i]:
                    currenciesoutput_list.append(currencies[i])
            return img_value
        else:
            print(f"Currency '{user_choiceinput}' not found in the list.")


def output_currency(img_value):
    while True:
        user_choiceoutput = input("Enter the currency for the output value: ")
        if user_choiceoutput in currency_dict:
            output_value = img_value * currency_dict[user_choiceoutput]
            print(output_value)
            break
        else:
            print(f"Currency '{user_choiceoutput}' not found in the list.")


#main_function
print(currencies)
img_result = input_currency()
print(currenciesoutput_list)
output_currency(img_result)
