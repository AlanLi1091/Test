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

df = pd.DataFrame({
    'Timestamps': timestamps,
    'Weir Flow(L/s)': wf_values,
    'Weir Level(cm)': wl_values,
})

df["Date and Time"] = df.Timestamps.apply(lambda x: x.replace('T', ' '))

new_df = df[['Date and Time', 'Weir Flow(L/s)', 'Weir Level(cm)']]

print(new_df)
export_csv = new_df.to_csv(r'C:\Users\allan\Desktop\githubtest\Test\Sanitary_Sewer_2_Modified.csv', index = None, header = True)

