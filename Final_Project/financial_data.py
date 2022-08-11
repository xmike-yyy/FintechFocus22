# from flask import request
# # import matplotlib as mpl
# # import matplotlib.pyplot as plt
# import math
# from flask import render_template

# form = request.form
# sales = form["sales"] #REVENUE = SALES
# sales = int(sales)
# cogs = form["cogs"]
# cogs = int(cogs)
# operatingexpenses = form["operatingexpenses"] 
# depamor = form["depamor"]
# ebit = form["ebit"] # Interest expense - taxes 
# operatingexpenses = int(operatingexpenses)
# depamor = int(depamor)
# ebit = int(ebit)


# grossprofit = sales - cogs
# operatingprofit = sales - cogs - operatingexpenses - depamor
# netprofit = operatingprofit - ebit

# financial_values = [
# # Gross Profit, Operating Profit, Net Profit   
# {"year": 1, "gross_profit" : 2000, "operating_profit" : 1000, "net_profit": 500},

# {"year": 2, "gross_profit" : 2500, "operating_profit" : 1500, "net_profit": 1000},
  
# {"year": 3, "gross_profit" : 3500, "operating_profit" : 2000, "net_profit": 1500},

# {"year": 4, "gross_profit" : grossprofit, "operating_profit" : operatingprofit, "net_profit": netprofit}
# ]


# years = []
# for item in financial_values:
#   years.append(item["year"])
# gprofit = []
# for item in financial_values:
#   gprofit.append(item["gross_profit"])
# oprofit = []
# for item in financial_values:
#   oprofit.append(item["operating_profit"])
# nprofit = []
# for item in financial_values:
#   nprofit.append(item["net_profit"])



# new_list = range(math.floor(min(years)), math.ceil(max(years))+1)

# plt.figure(1)
# plt.xticks(new_list)
# plt.plot(years, oprofit)
# plt.ylabel("Operating Profit")
# plt.xlabel("Year")
# plt.xlim([0, max(years)])
# plt.ylim([0, max(oprofit)+100])
# plt.savefig('oplot.png')

# plt.figure(2)
# plt.xticks(new_list)
# plt.plot(years, gprofit)
# plt.ylabel("Gross Profit")
# plt.xlabel("Year")
# plt.xlim([0, max(years)])
# plt.ylim([0, max(gprofit)+100])
# plt.savefig('gplot.png')


# plt.figure(3)
# plt.xticks(new_list)
# plt.plot(years, nprofit)
# plt.ylabel("Net Profit")
# plt.xlabel("Year")
# plt.xlim([0, max(years)])
# plt.ylim([0, max(nprofit)+100])
# plt.savefig('nplot.png')
  


