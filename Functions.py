import Dictionary as d


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
                        reference_value = ua / self.currency_dict[user_choiceinput]
                        break
                    else:
                        print("Enter a valid integer.")
                for i in range(len(d.currencies)):
                    if user_choiceinput != d.currencies[i]:
                        d.currenciesoutput_list.append(d.currencies[i])
                return reference_value
            else:
                print(f"Currency '{user_choiceinput}' not found in the list.")

    def output_currency(self, reference_value):
        while True:
            user_choice_output = input("Enter the currency for the output value: ")
            if user_choice_output in self.currency_dict:
                output_value = reference_value * self.currency_dict[user_choice_output]
                print(f"Converted value: {output_value:.2f} {user_choice_output}")
                break
            else:
                print(f"Currency '{user_choice_output}' not found in the list.")
