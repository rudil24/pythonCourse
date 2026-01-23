# rudil24
# squirrel_census.py
# 1. open the data (using pandas read)
# 2. get a count of each color of squirrels
# 3. create a dataframe with this info and save it as squirrel_count.csv
import pandas as pd

SQUIRREL_CSV = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260114.csv"

data = pd.read_csv(SQUIRREL_CSV)
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
}
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print(df)
