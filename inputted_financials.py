# --- IMPORT STATEMENTS ---
import business_data as businessdata
import financial_data as financialdata

# Add an input for "Gross Profit," "Operating Profit," and "Net Profit"
# Can use below for info if needed 
# https://m.foolcdn.com/media/affiliates/images/jeffries-office-service-income-statement_WzKhG.width-750.png 

# Name item 
Product = input("Product:")
NumberOfInventory = int(input("How many " + Product + "s do you have in inventory?"))
print("You have " + NumberOfInventory + " " + Product)
Price = int(input("How much are you selling one " + product + " for?"))
WorthOfProduct = NumberOfInventory * Price
Print("You have $" + WorthOfProduct + " worth of " + Product)

ProductB = input("ProductB:")
NumberOfInventoryB = int(input("How many " + ProductB + "s do you have in inventory?"))
print("You have " + NumberOfInventoryB + " " + ProductB)
PriceB = int(input("How much are you selling one " + ProductB + " for?"))
WorthOfProductB = NumberOfInventoryB * PriceB
Print("You have $" + WorthOfProductB + " worth of " + ProductB)
SoldProduct = int(input("How many " + Product + "s did you sell this month?"))
SoldProductB = int(input("How many " + ProductB + "s did you sell this month?"))
RevenuePerMonth = SoldProduct*Price + SoldProductB*PriceB
print("You made $" + RevenuePerMonth + " in revenue this month.")

# Input amount of item available
int(input((print("How many gatorades do you have in? "))))
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
