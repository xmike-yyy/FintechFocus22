import currencies
import requests
def assemble():
  function = True
  inner = True
  while function:
    start = input("What are you converting from? Crypto or currency? \n").lower()
    while inner: 
      if start == "crypto":
        print("Options: \n")
        print(currencies.cryptos)
        function = False
        break
      if start == "currency":
        print("Options: \n")
        print(currencies.physical_currencies)
        function = False
        break
      else:
        print("Invalid Input!")
        break
  function = True
  inner = True
  while function:
    fromc = input("")
    while inner:
      if fromc in currencies.physical_currencies.keys():
        ffromc = currencies.physical_currencies[fromc]
        function = False
        break
      elif fromc in currencies.cryptos.keys():
        ffromc = currencies.cryptos[fromc]
        function = False
        break
      else:
        print("Invalid input!")
        break
  print(ffromc)
  function = True
  inner = True
  if start == "crypto":
    print("Options: \n")
    print(currencies.physical_currencies)
  else:
    print("Options: \n")
    print(currencies.cryptos)
    
  to = input("What are you trying to convert into? \n").lower()
  while function:
    toc = ""
    while inner:
      if to in currencies.physical_currencies.keys():
        toc = currencies.physical_currencies[to]
        function = False
        break
      elif to in currencies.cryptos.keys():
        toc = currencies.cryptos[to]
        function = False
        break
      else:
        print("Invalid input!")
        break
  print(toc)
    # UTILIZE API TO RETREIVE VALUES FOR EXCHANGES
  value = input("How much do you want to convert? \n")
  if start == "crypto":
    one = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='
    two = '&to_currency='
    three = '&apikey=497MGRW5M4NV3OCE'
    url = one + ffromc + two + toc + three
    r = requests.get(url)
    data = r.json()
    rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    print(rate)
    perf = int(float(rate))
    rounded = round(perf)
    rvalue = int(value)*int(rounded)
    frvalue = int(rvalue)    
    print("You have converted " + str(value) + " of " + ffromc + " to $" + str(frvalue) + " amount of " + toc )
  else:
    one = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='
    two = '&to_currency='
    three = '&apikey=497MGRW5M4NV3OCE'
    url = one + toc + two + ffromc + three
    r = requests.get(url)
    data = r.json()
    rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    print(rate)
    perf = int(float(rate))
    rounded = round(perf)
    rvalue = float(value)/float(rounded)
    frvalue = str(rvalue)   
    print("You have converted " + str(value) + " of " + ffromc + " to " + frvalue + " amount of " + toc )
