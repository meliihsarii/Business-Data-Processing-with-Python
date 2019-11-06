import pandas as pd
import numpy as np
import os
filename = os.getcwd() + "\\Plaza Coffee.csv"
df = pd.read_csv(filename)
print(df)
print("Companies:", df.Company.unique())
print(df.Company.value_counts())
print("Order:", df.Order.unique())
print(df.Order.value_counts())
print("Quantity:", df.Quantity.unique())
print(df.Quantity.value_counts())
print("Payment:", df.Payment.unique())
print(df.Payment.value_counts())

companylist = [ "KPMG", "EY", "Deloite & Touche" ,"PWC"]
paymentlist= [ "Cash-Daily Menu(on discount)","Credit-Dailey Menu","Cash-Coffee(on discount)","Credit-Coffee","Cash-Dessert(on discount)","Credit-Dessert"]
consumptionlist = [7, 3, 4, 4,0]
dictionary = { "Company" : companylist, " Payment": paymentlist ,"Consumption":consumptionlist}

print("Company:", dictionary["Company"][0])
paymenlist= [ "Cash-Daily Menu","Credit-Dailey Menu","Cash-Coffee","Credit-Coffee","Cash-Dessert","Credit-Dessert"]
consumptionlist = [2, 2, 1, 3, 0,0]
zipped = zip(paymentlist,consumptionlist)
for name,coffee in zipped:
    print(name, " quantity equals to ", )      

print("Company:", dictionary["Company"][1])

paymenlist= [ "Cash-Daily Menu","Credit-Dailey Menu","Cash-Coffee","Credit-Coffee","Cash-Dessert","Credit-Dessert"]
consumptionlist = [1,1,0,3,0,0]
zipped = zip(paymentlist,consumptionlist)
for name,coffee in zipped:
    print(name, " quantity equals to ", coffee) 

print("Company:", dictionary["Company"][2])

paymenlist= [ "Cash-Daily Menu","Credit-Dailey Menu","Cash-Coffee","Credit-Coffee","Cash-Dessert","Credit-Dessert"]
consumptionlist = [1, 0, 1, 6, 1,0]
zipped = zip(paymentlist,consumptionlist)
for name,coffee in zipped:
    print(name, " quantity equals to ", coffee) 

print("Company:", dictionary["Company"][3])

paymenlist= [ "Cash-Daily Menu","Credit-Dailey Menu","Cash-Coffee","Credit-Coffee","Cash-Dessert","Credit-Dessert"]
consumptionlist = [2, 0, 1, 2, 0,0]
zipped = zip(paymentlist,consumptionlist)
for name,coffee in zipped:
    print(name, " quantity equals to ", coffee) 
 
  

