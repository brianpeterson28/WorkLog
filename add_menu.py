from screen import Screen

class Add_Menu(Screen):

    def __init__(self):
        self.title = "Work Log Program - Add Time Entry"
        self.options = None

    def show(self):
        print(self.title)
        print("")