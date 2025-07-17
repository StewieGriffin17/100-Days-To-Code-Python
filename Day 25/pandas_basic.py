# with open("./weather_data.csv") as data:
#     data_list = data.readlines()
#     print(data_list)

import csv

with open("./weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temp = []
    for row in data:
        if row[1] != "temp":
            temp.append(int(row[1]))
    print(temp)

import pandas

data = pandas.read_csv("/content/sample_data/weather_data.csv")
print(data)
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

# Average temp
temp_list = data['temp'].to_list()
sum = 0
for i in temp_list:
  sum += i
ave = sum / len(temp_list)
print(f"The average temperature is {ave}")

# Using mean function
ave2 = data['temp'].mean()
print(f"The average temperature is {ave2}")   

# Max temp
max_temp = data['temp'].max()
print(f"The maximum temperature is {max_temp}") 

# Getting a row
monday = data[data.day == "Monday"]
print(monday)

# Crating a dataframe from scratch
data_dict = {
    "Pirates": ["God D Usopp", "Con D Oriano", "Buggy D Clown"],
    "Bounty(in Billions)": [5.6, 4.9, 5.3]
}

data = pandas.DataFrame(data_dict)
print(data)
