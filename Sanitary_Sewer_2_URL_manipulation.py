import csv
import numpy as np
import pandas as pd
import json
from pandas import DataFrame

df = pd.read_csv("Sanitary_Sewer_2_Modified.csv")

weir_flow = df["Weir Flow(L/s)"]
weir_level = df["Weir Level(cm)"]
wl_array = np.array(weir_level)
wf_array = np.array(weir_flow)
wf_vs_wl = ([wf_array, wl_array])
wf_array_avg = np.mean(wf_array)
wf_array_avg2 = np.mean(wf_array > 15)
sorted_wf = np.sort(wf_array)
wf_array_median = np.median(wf_array)
#print(wf_array_avg)
#print(wf_array_avg2)
#print(sorted_wf)
print(wf_array_median)
