# Fixer: oqNtHS6H6GNbiCG3Q3lt69URjScijXXr
# Alpha Vantage API Key: 497MGRW5M4NV3OCE

# IMPORT STATEMENTS
import requests
import currencies
import convert

# PRINT DICTIONARY OF CRYPTOS AND CURRENCIES
print(currencies.cryptos)
print(currencies.physical_currencies)

# INPUT CURRENCIES 
x = input("\nWhat cryptocurrency you want to convert? ").lower()
y = input("What do you want to convert into? ").lower()

# RETREIVE AND PRINT CURRENCIES AND CRYPTOS
c = currencies.cryptos[x]
p = currencies.physical_currencies[y]
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

# UTILIZE API TO RETREIVE VALUES FOR EXCHANGES
one = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='
two = '&to_currency='
three = '&apikey=497MGRW5M4NV3OCE'
url = one + c + two + p + three
r = requests.get(url)
data = r.json()
# PRINT REQUESTED DATA TO USER
rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
print("You asked to convert " + x.upper() + " to " + y.upper() + ". The exchange rate is currently: " + str(rate) + ".")


# PROMPT USER TO SEE HOW MUCH THEY CAN EXCHANGE W/ CURRENT MONEY
option = input("\nYou want to see how much you can exchange: True or False? ").lower()
function = False
inner = True
if option == "true":
  convert.assemble()
else:
  print("Thank you for using!")

 



