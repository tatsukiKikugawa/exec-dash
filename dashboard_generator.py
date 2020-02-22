# dashboard_generator.py

import os
import pandas

#When the user runs the program, they should be prompted to select one of these CSV files to process.
#Validating user input

x = True
while x:
    selected_data = input("Please type the year and month of sales data you want to explore (Ex.201801): ")
    isValid = int(selected_data)
    if len(selected_data) != 6:
        print("Your input is too long or short. Use a valid input like 201801 with no space.")
        exit    
    elif isValid <= 201709:
        print("1Available data is from 201710 to 201904. Please try another year and month.")
        exit
    #elif isValid >= 201712 and isValid <=201801:
    #    print("2Available data is from 201710 to 201904. Please try another year and month.")
    #    exit
    #elif isValid >= 201812 and isValid <= 201901:
    #    print("3Available data is from 201710 to 201904. Please try another year and month.")
    #    exit
    elif isValid >= 201905:
        print("4Available data is from 201710 to 201904. Please try another year and month.")
        exit
    else:
        print("Valid Input")
        break
#Don't know how to deal with numbers between 201812 and 201901      

file_name = "sales-" + selected_data + ".csv"
print("READING SALES CSV FILE...")


csv_filepath = "monthly-sales/monthly-sales-data/" + file_name
print("FILEPATH:", os.path.dirname(__file__),csv_filepath)
products = pandas.read_csv(csv_filepath)
#print("PRODUCTS: ", type(products)) #><class 'pandas.core.frame.DataFrame'>

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")