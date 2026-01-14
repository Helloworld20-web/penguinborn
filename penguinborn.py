import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Very bad dataset for seaborn
seaboneds = pd.read_csv("penguins_size.csv")

#Matplot
seaboneds.plot(x="culmen_length_mm", y="culmen_depth_mm", marker='o', color="black")
plt.xlabel("culmen_length_mm")
plt.ylabel("culmen_depth_mm")
plt.show()

#Main Plots
sns.set_style("darkgrid")
sns.color_palette("viridis")

sns.scatterplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds)

sns.pairplot(seaboneds)

sns.relplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds, kind="scatter")

sns.lineplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds)

sns.displot(seaboneds, kind="ecdf")

sns.catplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds, kind="strip")

sns.catplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds, kind="violin")

sns.catplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds, kind="bar")

sns.catplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds, kind="point")

sns.lmplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds, hue="culmen_length_mm")

plt.show()

#Bar Plot
sns.barplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds)

plt.show()

#Gnome more heatmaps :(

# #Useless Stuff
sns.histplot(seaboneds, bins=10, kde=True)

sns.displot(seaboneds, kind="kde")

sns.displot(seaboneds, kind="hist")

sns.catplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds, kind="box")

sns.catplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds, kind="swarm")

sns.catplot(data=seaboneds, kind="count")

sns.regplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds)

plt.show()

#Uhh more stuff i guess

sns.boxplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds)

plt.show()

#Separatory Hashtag

plt.show()

sns.swarmplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds)

plt.show()

#Separatory Hashtag

sns.stripplot(x="culmen_length_mm", y="culmen_depth_mm", data=seaboneds)

plt.show()
