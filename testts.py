import csv
import re
import os
import datetime
from time_entry import Time_Entry

TIME_ENTRY_FILE = "time_entries.csv"

def clear_screen():
    """Clears the screen of all prior input and output."""

    os.system('cls' if os.name == 'nt' else 'clear')

def display_sr(count):
    if count == 0:
        print("Date: {}".format(matching_entries[count].date))
        print("Title: {}".format(matching_entries[count].title))
        print("Time Spent: {}".format(matching_entries[count].time_spent))
        print("Notes: {}".format(matching_entries[count].notes))
        print("")
        print("Result {} of {}".format(count + 1, total_results))
        print("")
        print("[N]ext, [E]dit, [D]elete, [R]eturn to search menu")
    elif count > 0:
        print("Date: {}".format(matching_entries[count].date))
        print("Title: {}".format(matching_entries[count].title))
        print("Time Spent: {}".format(matching_entries[count].time_spent))
        print("Notes: {}".format(matching_entries[count].notes))
        print("")
        print("Result {} of {}".format(count + 1, total_results))
        print("")
        print("[P]revious, [N]ext, [E]dit, [D]elete, [R]eturn to search menu")

time_entries = []
non_matching_entries = []
matching_entries = []

with open(TIME_ENTRY_FILE, newline="") as csvfile:
    time_entry_file = csv.reader(csvfile)
    for row in time_entry_file:
        entry = Time_Entry()
        entry.set_date(row[0])
        entry.set_title(row[1])
        entry.set_time_spent(row[2])
        entry.set_notes(row[3])
        time_entries.append(entry)

time_spent = 60

for entry in time_entries:
    if int(entry.time_spent) == time_spent:
        matching_entries.append(entry)
    else:
        non_matching_entries.append(entry)


total_results = len(matching_entries)
count = 0

while True:
    display_sr(count)
    dummy = input("> ")
    if dummy.upper() == "N":
        try:
            count += 1
            matching_entries[count]
        except IndexError:
            count -= 1
            clear_screen()
        clear_screen()
    elif dummy.upper() == "P":
        count -= 1
        if count < 0:
            count += 1
        clear_screen()
    elif dummy.upper == "E":
        pass
    elif dummy.upper() == "D":
        pass
    elif dummy.upper() == "R":
        pass
    else:
        break