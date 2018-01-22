from screen import Screen

class Main_Menu(Screen):

    def __init__(self):
        self.title = "Work Log Program - Main Menu"
        self.options = ["Add New Entry",
                        "Search Existing",
                        "Quit Program"]

    def show(self):
        print(self.title)
        print("")
        print("What would you like to do?")
        count = 1
        for item in self.options:
            print("{}) {}".format(count, item))
            count += 1
        count = 1

