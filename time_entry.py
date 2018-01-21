import datetime


class Time_Entry():

    def __init__(self, date=None, title="", time_spent=0, notes=""):
        self.date = date
        self.title = title
        self.time_spent = time_spent
        self.notes = notes
