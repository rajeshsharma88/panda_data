# with open("weather_data.csv") as data_file:
#     data = data_file.readline()
#     print(data)

#

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# #
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].tolist()
# print(len(temp_list))
#
# average = sum(temp_list)/(len(temp_list))
# print(average)
# print(data["temp"])
# print(data["temp"].max())
# print(data["temp"].mean())
# print(data.condition)

# print(data[data.day == "Monday"] )
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])
# monday = data[data.day == "Monday"]
# mon_temp = monday.temp
# temp_farenh = mon_temp * 9 / 5 + 32
# print(temp_farenh)

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_count)
print(red_count)
print(black_count)
data_dict ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_cont.csv")