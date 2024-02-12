# Place code below to do the analysis part of the assignment.

# Write a Python program in the file named analyze.py that does the following:
# opens up your cleaned up data file, clean_data.csv and imports it using Python's csv module.
# outputs the average temperature anomaly in degrees Farenheit for each decade since 1880. 
# For example, output the average temperature anomaly for the decades: 
# 1880 to 1889
# 1890 to 1899
# 1900 to 1909
# ...and so on.
# You are allowed to use the csv module to help parse your CSV data file in the analysis, 
# but not pandas or any other data parsing or analysis module.
import csv
f = open("data/clean_data.csv", "r")
csv_reader = csv.DictReader(f)

total_list = []
for line in csv_reader:
    total = 0
    for k in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
        if float(line['Year']) in range(1880, 1890):
            total += float(line[k])
        elif float(line['Year']) in range(1890, 1900):
            total += float(line[k])
        elif float(line['Year']) in range(1900, 1910):
            total += float(line[k])
        elif float(line['Year']) in range(1910, 1920):
            total += float(line[k])
        elif float(line['Year']) in range(1920, 1930):
            total += float(line[k])
        elif float(line['Year']) in range(1930, 1940):
            total += float(line[k])
        elif float(line['Year']) in range(1940, 1950):
            total += float(line[k])
        elif float(line['Year']) in range(1950, 1960):
            total += float(line[k])
        elif float(line['Year']) in range(1960, 1970):
            total += float(line[k])
        elif float(line['Year']) in range(1970, 1980):
            total += float(line[k])
        elif float(line['Year']) in range(1980, 1990):
            total += float(line[k])
        elif float(line['Year']) in range(1990, 2000):
            total += float(line[k])
        elif float(line['Year']) in range(2000, 2010):
            total += float(line[k])
        elif float(line['Year']) in range(2010, 2020):
            total += float(line[k])
        elif float(line['Year']) in range(2020, 2030):
            total += float(line[k])
    total_list.append(total)
    total = 0

decades_list = []
decades_avg = 0
for i in range(0, len(total_list),10):
    if i != 140:
        decades_avg += sum(total_list[i:i+10]) / len(total_list[i:i+10])
        decades_list.append(format(decades_avg, ".1f"))
    else:
        decades_avg += sum(total_list[i:]) / 4
        decades_list.append(format(decades_avg, ".1f"))
    decades_avg = 0

years = ["1880-1889", "1890-1899", "1900-1909", "1910-1919", "1920-1929", "1930-1939","1940-1949", "1950-1959", "1960-1969", "1970-1979","1980-1989", "1990-1999", "2000-2009", "2010-2019", "2020-2023"]
for y in range(len(decades_list)):
    print(years[y] + ": " + decades_list[y] + " F")
