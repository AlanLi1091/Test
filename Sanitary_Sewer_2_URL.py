import json
from urllib.request import urlopen
import csv
import pandas as pd
from pandas import DataFrame

with urlopen("https://developers.flowworks.com/fwapi/v1/c22cb202-f0ee-439b-97af-0c1b17e04f0a/site/8757/channel/1183/data/startdate/20191230000000/enddate/20200106") as ss2_wf_json:
    ss2_wf = json.load(ss2_wf_json)
with urlopen("https://developers.flowworks.com/fwapi/v1/c22cb202-f0ee-439b-97af-0c1b17e04f0a/site/8757/channel/1184/data/startdate/20191230000000/enddate/20200106") as ss2_wl_json:
    ss2_wl = json.load(ss2_wl_json)

ss2_wf_datapoints = ss2_wf["datapoints"]
ss2_wl_datapoints = ss2_wl["datapoints"]

wf_values = []
timestamps = []
wl_values = []
for datapoints in ss2_wf_datapoints:
    wf_values.append(datapoints["value"])
    timestamps.append(datapoints["date"])
    
for datapoints in ss2_wl_datapoints:
    wl_values.append(datapoints["value"])

date = []
time = []
for i in range(len(timestamps)):
    date.append(timestamps[i].split("T")[0])
    time.append(timestamps[i].split("T")[-1])

hrs_mins = []
for i in range(len(time)):
    hrs_mins.append(time[i][:-3])

df = pd.DataFrame({
    'Date': date,
    'Time': hrs_mins,
    'Weir Flow(L/s)': wf_values,
    'Weir Level(cm)': wl_values,
})

export_csv = df.to_csv(r'C:\Users\allan\Desktop\python-tcode\Sanitary_Sewer_2.csv', index = None, header = True)
print(df)
