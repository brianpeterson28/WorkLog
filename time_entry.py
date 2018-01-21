import csv

class Time_Entry():

    def __init__(self):
        self.date = ""
        self.title = ""
        self.time_spent = 0
        self.notes = ""

    def set_date(self, date):
        self.date = date

    def set_title(self, title):
        self.title = title

    def set_time_spent(self, time_spent):
        self.time_spent = time_spent

    def set_notes(self, notes):
        self.notes = notes

    def create_time_entry(self):
        entry = [self.date, self.title, self.time_spent, self.notes]
        with open("time_entries.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(entry)

