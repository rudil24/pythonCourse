import csv  # pre-installed python library for comma separated value files.

with open("weather_data.csv", newline="") as file:
    data = csv.reader(file, delimiter=",")
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

print(data)
import pandas  # need to install it, find it on pypi.org

# in pandas, a read_csv sheet is a data frame, a column of that data frame is a series

# for more info on what pandas can do, see https://pandas.pydata.org/docs/


data = pandas.read_csv("weather_data.csv")
# print(
#     data["temp"]
# )  # pandas reads the row headers and can access the data in each row underneath

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# below, print the mean temp of temp_list rounded to 2 decimal places
average = sum(temp_list) / len(temp_list)
print(round(average, 2))
print(
    round(data["temp"].mean(), 2)
)  # easier, use the mean method to get the average of the temp column
print(data["temp"].max())

# get data in columns
print(data["condition"])
print(data.condition)

# Get Data in Rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])  # print the row where the temp is the highest

monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp * 9 / 5 + 32)  # convert from celsius to fahrenheit
# or longer to just access the exact "cell" we want:
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
newdata = pandas.DataFrame(data_dict)
newdata.to_csv("new_data.csv")  # creates a new csv file
