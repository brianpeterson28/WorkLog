#import csv
#import os
from time_entry import Time_Entry

entry1 = Time_Entry()
entry2 = Time_Entry()

entry1.set_date("1-1-2018")
entry1.set_title("Github Desktop")
entry1.set_time_spent("10 Minutes")
entry1.set_notes("Created Github respository.")

entry2.set_date("6-15-2018")
entry2.set_title("Cool Uncle")
entry2.set_time_spent("1 Hour")
entry2.set_notes("Listened to Music.")

entry1.create_time_entry()
entry2.create_time_entry()

'''
def clear_screen():
    """Clears the screen of all prior input and output."""

    os.system('cls' if os.name == 'nt' else 'clear')
'''