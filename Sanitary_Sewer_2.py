import json
import pandas as pd

with open('sanitary_sewer_2_weir_flow_191230_200106.json', 'r') as ss2_wf_json:
    ss2_wf = json.load(ss2_wf_json)

with open('sanitary_sewer_2_weir_level_191230_200106.json', 'r') as ss2_wl_json:
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

# Values: Dates, time in hours and minutes, weir flow values, and weir level values

df = pd.DataFrame({
    'Date': date,
    'Time': hrs_mins,
    'Weir Flow(L/s)': wf_values,
    'Weir Level(cm)': wl_values,
})

print(df)
