import csv
import re

TIME_ENTRY_FILE = "time_entries.csv"

time_entries = []
str_time_entries = ""
with open(TIME_ENTRY_FILE, newline="") as csvfile:
    time_entry_file = csv.reader(csvfile)
    for row in time_entry_file:
        time_entries.append(row)
    for item in time_entries:
        str_time_entries += str(item)
    print(str_time_entries)
    variable = re.findall(r'08/06/2016', str_time_entries)
    print(variable)

