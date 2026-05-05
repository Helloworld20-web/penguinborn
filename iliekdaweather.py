import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

mmcsv = pd.read_csv("Weather Dataset.csv")

print(f"Csv file opened in pandas: {mmcsv}\n")

print(f"Csv file opened with more rows shown: {mmcsv.head(20)}\n")

print(f"Csv file opened from the bottom: {mmcsv.tail()}\n")

print(f"Csv file's info {mmcsv.info()}\n")

print(f"Csv file's described {mmcsv.describe()}\n")

print(f"Csv file's shape {mmcsv.shape}\n")

print(f"Csv file's columns {mmcsv.columns}\n")

print(f"Csv file's index(rows) {mmcsv.index}\n")