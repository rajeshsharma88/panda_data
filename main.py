# with open("weather_data.csv") as data_file:
#     data = data_file.readline()
#     print(data)

#

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data["temp"])


