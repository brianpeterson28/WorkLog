import os
from time_entry import Time_Entry
from main_menu import Main_Menu
from add_menu import Add_Menu


def main():
    while True:
        choice = run_main_menu_process()
        if choice == "1":
            run_add_entry_process()
        if choice == "2":
            pass
        if choice == "3":
            break

def run_main_menu_process():
    clear_screen()
    main = Main_Menu()
    main.show()
    main_result = input("Please enter number of choice (e.g. 1): ")
    clear_screen()
    return main_result

def run_add_entry_process():
    entry = Time_Entry()
    add = Add_Menu()
    add.show()
    print("Date of the Task")
    date = input("Please use DD/MM/YYYY format: ")
    entry.set_date(date)
    clear_screen()
    add.show()
    title = input("Title of Task: ")
    entry.set_title(title)
    clear_screen()
    add.show()
    time_spent = input("Time spent (rounded in minutes): ")
    entry.set_time_spent(time_spent)
    clear_screen()
    add.show()
    notes = input("Notes (Optional, you can leave this empty): ")
    entry.set_notes(notes)
    entry.create_time_entry()
    clear_screen()
    input("The entry has been added! Press enter to return to main menu.")
    clear_screen()

def clear_screen():
    """Clears the screen of all prior input and output."""

    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()