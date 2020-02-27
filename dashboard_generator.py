# dashboard_generator.py

import os
import csv
import pandas
import plotly
import plotly.graph_objs as go

def to_usd(my_price):
    # return "${0:,.2f}".format(my_price)
    return f"${my_price:,.2f}"

#
#INFO INPUTS with Validation
#

x = True
while x:
    selected_data = input("Please type the year and month of sales data you want to explore (Ex.201801): ")
    isValid = int(selected_data)
    if len(selected_data) != 6:
        print("Your input is too long or short. Use a valid input like 201801 with no space.")
        exit    
    elif isValid <= 201709:
        print("Hey, didn't find a file. Available data is from 201710 to 201904. Please try another year and month.")
        exit
    #elif isValid >= 201712 and isValid <=201801:
    #    print("2Available data is from 201710 to 201904. Please try another year and month.")
    #    exit
    #elif isValid >= 201812 and isValid <= 201901:
    #    print("3Available data is from 201710 to 201904. Please try another year and month.")
    #    exit
    elif isValid >= 201905:
        print("Hey. didn't find a file. Available data is from 201710 to 201904. Please try another year and month.")
        exit
    else:
        print("Valid Input")
        break
#Don't know how to deal with numbers between 201812 and 201901      

csv_filename = "sales-" + selected_data + ".csv"

csv_filepath = "monthly-sales/monthly-sales-data/" + csv_filename
#print("FILEPATH:", os.path.dirname(__file__), csv_filepath)
csv_data = pandas.read_csv(csv_filepath)
#print("PRODUCTS: ", type(products)) #><class 'pandas.core.frame.DataFrame'>

#
# CALCULATIONS
#

monthly_total = csv_data["sales price"].sum()
product_totals = csv_data.groupby(["product"]).sum()
print("READING SALES CSV FILE...")

product_totals = product_totals.sort_values("sales price", ascending=False)

top_sellers = []
rank = 1
for i, row in product_totals.iterrows():
    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
    top_sellers.append(d)
    rank = rank + 1


#
# OUTPUT
#
print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {monthly_total}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
for d in top_sellers:
    print("  " + str(d["rank"]) + ") " + d["name"] +
          ": " + to_usd(d["monthly_sales"]))

print("-----------------------")

labels = [d["name"] for d in top_sellers]
values = [d["monthly_sales"] for d in top_sellers]

trace = go.Pie(labels=labels, values=values)

plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)