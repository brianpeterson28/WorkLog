import os
import datetime
import csv
import re
from time_entry import Time_Entry
from main_menu import Main_Menu
from add_menu import Add_Menu
from search_menu import Search_Menu

TIME_ENTRY_FILE = "time_entries.csv"

def main():
    while True:
        choice = run_main_menu_process()
        if choice == "1":
            run_add_entry_process()
        if choice == "2":
            search = Search_Menu()
            search.show()
            search_type = input("Please select a search type: ")
            clear_screen()
            if search_type.lower() == "a":
                run_exact_date_search_process()
            elif search_type.lower() == "b":
                run_range_of_dates_search_process()
            elif search_type.lower() == "c":
                run_time_spent_process()
            elif search_type.lower() == "d":
                run_exact_search_process()
            elif search_type.lower() == "e":
                run_regex_process()
            elif search_type.lower() == "f":
                pass
            else:
                print("The search option you entered is not recognized.")
                print("Please enter a letter corresponding to an availble" +
                "option, e.g. \"a\"")
                print("")
                dummy = input("Press enter to return to main menu. ")
        if choice == "3":
            break

def run_regex_process():
    print("This will search for matches in the title and notes fields.")
    regex_pattern = input("Enter a valid regex pattern: ")
    time_entries = recall_time_entries()
    matching_entries = []
    non_matching_entries = []
    for entry in time_entries:
        if re.search(r'' + regex_pattern, entry.title + entry.notes):
            matching_entries.append(entry)
        else:
            non_matching_entries.append(entry)
    clear_screen()
    if len(matching_entries) == 0:
        print("No matching entries found.")
        dummy = input("Press enter to continue. ")
    else:
        run_options_loop(matching_entries)

def run_exact_search_process():
    print("This will search for matches in the title and notes fields.")
    search_term = input("Enter a search term: ")
    time_entries = recall_time_entries()
    matching_entries = []
    non_matching_entries = []
    for entry in time_entries:
        if re.search(r'' + search_term, entry.title + entry.notes):
            matching_entries.append(entry)
        else:
            non_matching_entries.append(entry)
    clear_screen()
    if len(matching_entries) == 0:
        print("No matching entries found.")
        dummy = input("Press enter to continue. ")
    else:
        run_options_loop(matching_entries)


def run_time_spent_process():
    print("Enter the amount of time spent")
    time_spent = input("Please use the number of minutes (e.g. 60): ")
    time_entries = recall_time_entries()
    matching_entries = []
    non_matching_entries = []
    for entry in time_entries:
        if int(entry.time_spent) == int(time_spent):
            matching_entries.append(entry)
        else:
            non_matching_entries.append(entry)
    clear_screen()
    if len(matching_entries) == 0:
        print("No matching entries found.")
        dummy = input("Press enter to continue. ")
    else:
        run_options_loop(matching_entries, non_matching_entries)


def run_range_of_dates_search_process():
    print("Enter the Start Date of Range")
    start_date = input("Please use DD/MM/YYYY format: ")
    clear_screen()
    print("Enter the End Date of Rnage")
    end_date = input("Please use DD/MM/YYYY format: ")
    start_date = datetime.datetime.strptime(start_date,'%d/%m/%Y')
    end_date = datetime.datetime.strptime(end_date, '%d/%m/%Y')
    time_entries = recall_time_entries()
    matching_entries = []
    non_matching_entries = []
    for entry in time_entries:
        entry_date = datetime.datetime.strptime(entry.date, '%d/%m/%Y')
        if entry_date > start_date and entry_date < end_date:
            matching_entries.append(entry)
        else:
            non_matching_entries.append(entry)
    clear_screen()
    if len(matching_entries) == 0:
        print("No matching entries found.")
        dummy = input("Press enter to continue. ")
    else:
        run_options_loop(matching_entries)


def run_exact_date_search_process():
    print("Enter the Date")
    exact_date = input("Please use DD/MM/YYYY: ")
    time_entries = recall_time_entries()
    matching_entries = []
    non_matching_entries = []
    for entry in time_entries:
        if re.match(r'' + exact_date, entry.date):
            matching_entries.append(entry)
        else:
            non_matching_entries.append(entry)
    clear_screen()
    if len(matching_entries) == 0:
        print("No matching entries found.")
        dummy = input("Press enter to continue. ")
    else:
        run_options_loop(matching_entries)

def run_options_loop(matching_entries, non_matching_entries):
    total_results = len(matching_entries)
    count = 0
    while True:
        display_sr(matching_entries, count, total_results)
        option = input("> ")
        if option.upper() == "N":
            try:
                count += 1
                matching_entries[count]
            except IndexError:
                count -= 1
                clear_screen()
            clear_screen()
        elif option.upper() == "P":
            count -= 1
            if count < 0:
                count += 1
            clear_screen()
        elif option.upper() == "E":
            clear_screen()
            while True:
                print("What field would you like to edit?")
                print("Please type \"date\", \"title\", \"time spent\", or " + 
                      "\"notes\".")
                print("")
                edit_selection = input("> ")
                clear_screen()
                edit_selection.lower().strip()
                if edit_selection == "date":
                    print("Enter a new date.")
                    print("Please use DD/MM/YYYY format.")
                    new_date = input("> ")
                    matching_entries[count].set_date(new_date)
                    save_edited_entry(matching_entries, non_matching_entries) 
                    clear_screen()
                    break
                elif edit_selection == "title":
                    dummy = input("Press enter.")
                    break
                elif edit_selection == "time spent":
                    dummy = input("Press enter.")
                    break
                elif edit_selection == "notes":
                    dummy = input("Press enter.")
                    break
                else:
                    print("The field you entered is not recognized.")
                    dummy = input("Press enter to try again.")
                    clear_screen()
        elif option.upper() == "D":
            pass
        elif option.upper() == "R":
            break
        else:
            break     

def save_edited_entry(matching_entries, non_matching_entries):
    edited_entries = matching_entries + non_matching_entries
    first = create_iterable_entry(edited_entries.pop(0))

    with open(TIME_ENTRY_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(first)

    with open(TIME_ENTRY_FILE, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for entry in edited_entries:
            entry = create_iterable_entry(entry)
            writer.writerow(entry)

def create_iterable_entry(entry):
    iterable_entry = []
    iterable_entry.append(entry.date)
    iterable_entry.append(entry.title)
    iterable_entry.append(entry.time_spent)
    iterable_entry.append(entry.notes)
    return iterable_entry

def display_sr(matching_entries, count, total_results):
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


def recall_time_entries():
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
    return time_entries

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