import Functions as f
import Dictionary as d

# Main Function: 
converter = f.CurrencyConverter(d.currency_dict)
print(d.currencies)
refrence_value = converter.input_currency()
print(d.currenciesoutput_list)
converter.output_currency(refrence_value)




