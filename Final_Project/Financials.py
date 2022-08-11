# Add an input for "Gross Profit," "Operating Profit," and "Net Profit"
# Can use below for info if needed 
# https://m.foolcdn.com/media/affiliates/images/jeffries-office-service-income-statement_WzKhG.width-750.png 

# Name item 
Product = input("Product: ")
NumberOfInventory = int(input("How many " + Product + "s do you have in inventory? "))
Price = int(input("How much are you selling one " + Product + " for? "))
WorthOfProduct = NumberOfInventory * Price
print("You have $" + str(WorthOfProduct) + " worth of " + Product)
ProductB = input("ProductB: ")
NumberOfInventoryB = int(input("How many " + ProductB + "s do you have in inventory? "))
print("You have " + str(NumberOfInventoryB) + " " + ProductB)
PriceB = int(input("How much are you selling one " + ProductB + " for? "))
WorthOfProductB = NumberOfInventoryB * PriceB
print("You have $" + str(WorthOfProductB) + " worth of " + ProductB)
SoldProduct = int(input("How many " + Product + "s did you sell this month? "))
SoldProductB = int(input("How many " + ProductB + "s did you sell this month? "))
RevenuePerMonth = SoldProduct*Price + SoldProductB*PriceB
print("You made $" + str(RevenuePerMonth) + " in revenue this month.")

print(" ")
print(" ")
print(" ")

CostProduct = int(input(("How much do you spend on one " + Product + ": ")))
print("you spent $" + str(CostProduct * NumberOfInventory) + " on " + Product)
CostProductB = int(input("How much do you spend on one " + ProductB + ": "))
print("you spend $" + str(CostProductB * NumberOfInventoryB) + " on " + ProductB)
CostPerMonth = CostProduct + CostProductB
ProfitPerMonth = RevenuePerMonth - CostPerMonth
print(" ")
print(" ")
print(" Monthly Revenue: $" + str(RevenuePerMonth) )
print(" Monthly Costs: $" + str(CostPerMonth) )
print(" Monthly Profits: $" + str(ProfitPerMonth))

# Input amount of item available
# Input the price you selling something at
# Multiply the price by amount sold
 # Do for all inventory items
# Set that equal to revenue


# Put costs one by one (rent + utilities + employee payments)
# Do revenue - costs
# If positive, set that equal to profit
# If negative, set that equal to deficit
# 



# If the item is selling less than previous weeks send a suggestion, maybe suggest a disount or promotional sale (mvp 3)


for profit
  return revenue - cost 
