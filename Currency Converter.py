currency_dict = {'Rupees': 10.00, 'Dollar': 0.12, 'BTC': 0.0000019, 'CAD': 0.16, 'NZD': 0.20, 'EGP': 5.73, 'AED': 0.44, 'AUD': 0.18, 'SK': 20.0}
currencies = ['Rupees', 'Dollar', 'BTC', 'CAD', 'NZD', 'EGP', 'AED', 'AUD']
currenciesoutput_list = []

class CurrencyConverter:
    def __init__(self, currency_dict):
        self.currency_dict = currency_dict

    def input_currency(self):
        while True:
            user_choiceinput = input("Enter the currency you want to input: ")
            if user_choiceinput in self.currency_dict:
                while True:
                    user_amt = input("Enter the amount you want to convert: ")
                    if user_amt.isdigit():
                        ua = int(user_amt)
                        refrence_value = ua / self.currency_dict[user_choiceinput]
                        break
                    else:
                        print("Enter a valid integer.")
                for i in range(len(currencies)):
                    if user_choiceinput != currencies[i]:
                        currenciesoutput_list.append(currencies[i])
                return refrence_value
            else:
                print(f"Currency '{user_choiceinput}' not found in the list.")

    def output_currency(self, reference_value):
        while True:
            user_choiceoutput = input("Enter the currency for the output value: ")
            if user_choiceoutput in self.currency_dict:
                output_value = reference_value * self.currency_dict[user_choiceoutput]
                print(f"Converted value: {output_value:.2f} {user_choiceoutput}")
                break
            else:
                print(f"Currency '{user_choiceoutput}' not found in the list.")

# Main Function: 
converter = CurrencyConverter(currency_dict)
print(currencies)
refrence_value = converter.input_currency()
print(currenciesoutput_list)
converter.output_currency(refrence_value)




