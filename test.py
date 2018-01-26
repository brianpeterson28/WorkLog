import csv
import re
from time_entry import Time_Entry

TIME_ENTRY_FILE = "time_entries.csv"

time_entries = []
with open(TIME_ENTRY_FILE, newline="") as csvfile:
    time_entry_file = csv.reader(csvfile)
    for row in time_entry_file:
        entry = Time_Entry()
        entry.set_date(row[0])
        entry.set_title(row[1])
        entry.set_time_spent(row[2])
        entry.set_notes(row[3])
        time_entries.append(entry)

for index in range(len(time_entries)):
    print(time_entries[index].date + ", " 
          + time_entries[index].title + ", " 
          + time_entries[index].time_spent + ", " 
          + time_entries[index].notes)
print("")
print(time_entries)
print("")
if re.match(r'08/06/2016', time_entries[2].date):
    print("Ha ha ha! This works.")
    print("")
    print(time_entries[2].date + ", " 
          + time_entries[2].title + ", " 
          + time_entries[2].time_spent + ", " 
          + time_entries[2].notes)
#variable = re.findall(r'08/06/2016', str_time_entries)


