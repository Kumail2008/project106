import csv
import plotly.express as px
import pandas as pd
import numpy as n


def getDataSource(data_path):
    iceCream_sales = []
    coldDrink_sales = []
    temperature = []
    with open(data_path) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
#make sure that the csv's column name does not have spaces      
#check if the data type is float or integer       
            temperature.append(int(row["Coffee"]))
            iceCream_sales.append(int(row["Sleep"]))
    return{
        "x":temperature,
        "y":iceCream_sales
    }

def findCorrelation(data_source):
    correlation = n.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between coffee and sleep is: ",correlation[0,1])

def setup():
    data_path = "coffee.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()