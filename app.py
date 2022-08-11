# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
# import financial_data
from flask import render_template
from flask import request
import os


# -- Initialization section --
keep = Flask(__name__)

# -- Routes section --
@keep.route('/')
@keep.route('/index')
def index():
    #create data to send to index.html
    userinfo = {
      'user':{"first_name":"BananaBees",
             "industry":"Restaurant and Food Services"
             }
    }
    
    return render_template("index.html", userinfo=userinfo)

@keep.route("/myFinances", methods=["GET", "POST"])
def compute_finances():
  if request.method == "POST":
    form = request.form
    sales = form["sales"] #REVENUE = SALES
    sales = int(sales)
    cogs = form["cogs"]
    cogs = int(cogs)
    operatingexpenses = form["operatingexpenses"] 
    depamor = form["depamor"]
    ebit = form["ebit"] # Interest expense - taxes 
    operatingexpenses = int(operatingexpenses)
    depamor = int(depamor)
    ebit = int(ebit)
    
# --- MATH ---

    grossprofit = sales - cogs
    operatingprofit = sales - cogs - operatingexpenses - depamor
    netprofit = operatingprofit - ebit

# --- DATA --- 
    financial_values = [
    # Gross Profit, Operating Profit, Net Profit   
    {"year": 1, "gross_profit" : 2000, "operating_profit" : 1000, "net_profit": 500},
    
    {"year": 2, "gross_profit" : 2500, "operating_profit" : 1500, "net_profit": 1000},
      
    {"year": 3, "gross_profit" : 3500, "operating_profit" : 2000, "net_profit": 1500},
    
    {"year": 4, "gross_profit" : grossprofit, "operating_profit" : operatingprofit, "net_profit": netprofit}
    ]
    
# --- SUGGESTIONS --- 
    # financial_values = financial_data.financial_values
    lossadvice = "It looks like you're current running in a loss. No worries try some of our resources."
    link1 = "https://www.forbes.com/sites/mikekappel/2017/05/03/5-causes-for-a-small-business-losing-money/"
    link2 = "https://www.prospa.com/blog/5-ways-stop-your-business-losing-money"
    link3 = "https://www.consultstraza.com/5-ways-your-small-business-may-be-losing-money-and-how-to-stop-it/"

    stagnantadvice = "You're on the right track! Here are some resources that'll help your growth."
    link4 = "https://smallbiztrends.com/2018/04/how-to-grow-your-small-business.html"
    link5 = "https://www.nytimes.com/guides/business/how-to-grow-your-business"
    link6 = "https://www.entrepreneur.com/article/306049"

    growthadvice = "It looks like you're growing quickly! Here are some articles to maintain that growth."
    link7 = "https://www.forbes.com/sites/glennllopis/2015/09/29/top-6-ways-to-sustain-business-growth/"
    link8 = "https://www.bdc.ca/en/articles-tools/business-strategy-planning/manage-growth/9-tips-handling-fast-business-growth"
    link9 = "https://hbr.org/1983/05/the-five-stages-of-small-business-growth"
    if netprofit <= 0:
      advice = lossadvice
      image1 = "bgplot.png"
      image2 = "bnplot.png"
      image3 = "boplot.png"
    elif netprofit * 1.05 >= financial_values[3]["net_profit"]: 
      link1 = link7
      link2 = link8
      link3 = link9
      advice = growthadvice
      image1 = "gplot.png"
      image2 = "nplot.png"
      image3 = "oplot.png"
    elif financial_values[3]*0.95 <= netprofit < financial_values[3]*1.05: 
      link1 = link4
      link2 = link5
      link3 = link6
      advice = stagnantadvice
    else: 
      link1 = link4
      link2 = link5
      link3 = link6
      advice = stagnantadvice

 # --- PROFIT & GROWTH ---   

    operatingprofit = f"Your Operating Profit for Y4 is ${operatingprofit}."
    netprofit = f"Your net profit for Y4 is ${netprofit}."
    grossprofit = f"Your gross profit for Y4 is ${grossprofit}."

    
# --- SEND DATA TO HTML --- 
    return render_template("/results.html", operatingprofit = operatingprofit, netprofit=netprofit, grossprofit=grossprofit, link1=link1, link2=link2, link3=link3, advice=advice)

# --- IF THEY DONT ENTER ANYTHING
  elif request.method == "GET":
    return f"\n          Hello. You're getting the financial analysis page, but your data seems to be out of date."



keep.run(host='0.0.0.0', port=81, debug=True)