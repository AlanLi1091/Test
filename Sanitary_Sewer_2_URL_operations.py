import csv
import json
import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("Sanitary_Sewer_2_Modified.csv")


#x = df['Date and Time']
#y = df["Weir Flow(L/s)"]
#ax = plt.subplot()
#plt.plot(x, y)
#plt.xlabel("Date and Time")
#plt.ylabel("Weir Flow(L/s)")
#plt.title("Weir Flow Graph")
#ax.set_xticks(["2019-12-30 00:00:00", "2019-12-31 00:00:00", "2020-01-01 00:00:00", "2020-01-02 00:00:00", "2020-01-03 00:00:00", "2020-01-04 00:00:00", "2020-01-05 00:00:00", "2020-01-06 00:00:00"])
#plt.show()

#x = df['Date and Time']
#y = df["Weir Level(cm)"]
#ax = plt.subplot()
#plt.plot(x, y, color='red')
#plt.xlabel("Date and Time")
#plt.ylabel("Weir Level(cm)")
#plt.title("Weir Level Graph")
#ax.set_xticks(["2019-12-30 00:00:00", "2019-12-31 00:00:00", "2020-01-01 00:00:00", "2020-01-02 00:00:00", "2020-01-03 00:00:00", "2020-01-04 00:00:00", "2020-01-05 00:00:00", "2020-01-06 00:00:00"])
#plt.show()

#x = df["Weir Flow(L/s)"]
#y = df["Weir Level(cm)"]
#ax = plt.subplot()
#plt.scatter(x, y, c="green", alpha=0.6)
#plt.xlabel("Weir Flow(L/s)")
#plt.ylabel("Weir Level(cm)")
#plt.title("Weir Level vs Weir Flow Graph")
#ax.set_xticks(range(0, 41, 2))
#ax.set_yticks(range(0, 19, 2))
#plt.show()

#ax = plt.subplot
#plt.bar(range(len(df["Date and Time"])), df["Weir Flow(L/s)"])
#plt.title("Weir Flow Bar Graph")
#plt.xlabel("Index")
#plt.ylabel("Weir Flow(L/s)")
#plt.show()

#ax = plt.subplot
#plt.bar(range(len(df["Date and Time"])), df["Weir Level(cm)"], color="red")
#plt.title("Weir Level Bar Graph")
#plt.xlabel("Index")
#plt.ylabel("Weir Level(cm)")
#plt.show()

ax = plt.subplot
plt.hist(df["Weir Flow(L/s)"], bins=40)
plt.title("Recorded Weir Flow Distributions")
plt.xlabel("Recorded Weir Flow(L/s)")
plt.ylabel("Number of Recordings")
plt.show()

ax = plt.subplot
plt.hist(df["Weir Level(cm)"], bins=20, color="red")
plt.title("Recorded Weir Level Distributions")
plt.xlabel("Recorded Weir Level(L/s)")
plt.ylabel("Number of Recordings")
plt.show()