"""
Initial code for scope and linking to
google sheets taken from love-sandwiches
walkthrough by code institute
"""
from time import sleep
import os
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('EQ6453 Intake Forms')

forms_sheet = SHEET.worksheet("forms")
forms_data = forms_sheet.get_all_values()
forms_dict = forms_sheet.get_all_records()
data_frame = pd.DataFrame(forms_sheet.get_all_values())
class_size = 22
main_options = None


def login():
    """
    get username and staff number input from user.
    error message will appear if data invalid
    If valid will bring user to main menu
    while loop so that if incorrect input loop will
    request input from user again until valid data entered
    """
    while True:
        name = input("Enter your name with no spaces: \n")
        if validate_name(name):
            print("Data is valid\n")
            break

    while True:
        staff_number = input("Enter your 8 digit staff number: \n")
        if validate_staff_number(staff_number):
            print("Data is valid\n")
            break


def validate_name(name):
    """
    Raises value error if name is not letter.
    """
    try:
        if not name.isalpha():
            raise ValueError(
                "no symbols, numbers or spaces allowed"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False
    return True


def validate_staff_number(staff_number):
    """
    Raises ValueError if there arent exactly 8 values in staffnumber
    Raises ValueError if staffnumber is not numeric
    """
    try:
        if not staff_number.isnumeric():
            raise ValueError(
                "non numeric value entered in staff number"
                )
        if len(staff_number) != 8:
            raise ValueError(
                f"8 digits required for staff no. {len(staff_number)} entered"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False

    return True


def main_menu():
    """
    Main menu
    Options 1,2,3,4
    while loop so that if incorrect input loop will
    request input from user again until valid data entered
    """
    show_menu = True
    while show_menu:
        print("\nMain Menu")
        print("Enter 1, 2, 3 or 4 for the following options:\n")
        print("1 - Forms Outstanding ")
        print("2 - Medical declarations")
        print("3 - Levels of riders")
        print("4 - Exit\n")
        option_invalid = True
        while option_invalid:
            main_options = input("Option: \n")
            option_invalid = not validate_main_menu(main_options)
        os.system('cls' if os.name == 'nt' else 'clear')
        if main_options == '1':
            forms()
        elif main_options == '2':
            medical()
        elif main_options == '3':
            rider_levels()
        elif main_options == '4':
            print("Exiting...")
            show_menu = False


def validate_main_menu(main_options):
    """
    Raises ValueError if input is not '1', '2', '3' or '4'
    """
    try:
        if (main_options) not in ('1', '2', '3', '4'):
            raise ValueError(
                "Enter 1,2,3 or 4:"
            )
    except ValueError as e:
        print(f"Invalid data: {e} please try again.\n")
        return False

    return True


def forms():
    """
    Counts rows of data in forms sheet and
    subtracts 1 so headings row is not counted
    subracts this from class size to get value for outstanding forms
    """
    print("No. of forms outstanding:")
    submitted_forms = len(forms_data) - 1
    outstanding_forms = class_size - submitted_forms
    print(
        f"{submitted_forms} forms submitted.\
        {outstanding_forms} forms outstanding.\n"
        )
    sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')


def medical():
    """
    Checks which students have medical declarations
    Returns list with name and details from relevant
    columns of students who have declared a medical condition
    """
    print("Students with medical declarations:")
    df_medical = data_frame.iloc[1:, [0, 8, 9, 10]]
    df_string = df_medical[8].str.contains(" ")
    # PEP8 error: (158: E712 comparison to True should be 'if cond is True)
    medical_true = df_medical[df_string.values == True]
    print("\nMedical Details and if Doctor approved participation:\n")
    medical_details = medical_true.values.tolist()
    for detail in medical_details:
        print("**************************************************")
        print(f"{detail[0]} - {detail[1]} ? \n")
        print(f"{detail[2]} - Doctor Appproved ? : {detail[3]}")
        print("************************************************** \n")
    sleep(12)
    os.system('cls' if os.name == 'nt' else 'clear')


def rider_levels():
    """
    Returns columns with index of 0 and 12
    rider names and their level
    These are printed to the terminal and the number of
    students in each level
    """
    df_levels = data_frame.iloc[1:, [0, 12]]
    beginner = df_levels[df_levels.values == 'Beginner']
    novice = df_levels[df_levels.values == 'Novice']
    intermediate = df_levels[df_levels.values == 'Intermediate']
    advanced = df_levels[df_levels.values == 'Advanced']
    print("\nNumber of riders in each level:")
    print(f"\n--{len(beginner)} BEGINNER RIDERS--")
    print(beginner)
    print(f"\n--{len(novice)} NOVICE RIDERS--")
    print(novice)
    print(f"\n--{len(intermediate)} INTERMEDIATE RIDERS--")
    print(intermediate)
    print(f"\n--{len(advanced)} ADVANCED RIDERS--")
    print(advanced)
    sleep(12)
    os.system('cls' if os.name == 'nt' else 'clear')

login()
main_menu()

# if __name__ == "__main__":