import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

mmcsv = pd.read_csv("Salary.csv")

sns.barplot(x="YearsExperience",y="Salary", data=mmcsv)

plt.show()

sns.lineplot(x="YearsExperience",y="Salary", data=mmcsv)