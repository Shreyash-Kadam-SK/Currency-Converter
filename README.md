# Currency-Converter
Currency Converter 

Currency converter using different logic
- 1 dictionary used for all calculations
- By using a reference value which is 10 rupees mathematicaly
- A reference value is created then it is related to all the currencies and dictionary has the ratio to convert any given currency to reference value
- Then again using the dictionary reference value is converted to any currency as the user wants.
- The Dictionary is {'Rupees': 10.00, 'Dollar': 0.12, 'BTC': 0.0000019, 'CAD': 0.16, 'NZD': 0.20, 'EGP': 5.73, 'AED': 0.44,
                 'AUD': 0.18} 
- The logic behind it is dictionary has values to convert any currency to reference value and back from reference value to currency 
- So to convert rupees to reference value is[rupees/10.00(10 is the value assigned in dictionary to rupees)=reference value]
- And to convert reference value to Dollar is[reference value*0.12(0.12 is the value assigned in dictionary to Dollar)=Dollar]
                                              -Reference logic by me