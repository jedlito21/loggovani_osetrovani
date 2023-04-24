from tkinter import *
import pandas as pd
import logging
import csv

file = pd.read_csv("nums.csv")


citatele = file.iloc[:, 0].values
print(citatele)
print("----------------")
jmenovatele = file.iloc[:, 1].values
print(jmenovatele)
print("-----------------------------------")


for citatel in citatele:
    print(citatel)
for jmenovatel in jmenovatele:
    print(jmenovatel)
    print("-------*****************--------------------------")
    try:
        vysledek = int(citatel) / int(jmenovatel)
        print(vysledek)
    except:
        print("Něco")



