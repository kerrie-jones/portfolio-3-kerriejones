from pprint import pprint as pp
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
df = pd.DataFrame(forms_sheet.get_all_values())
eq453_class_size = 22


# levels = SHEET.worksheet("levels")
# medical = SHEET.worksheet("medical")


def login():
    """
    get username and staff number input from user.
    error message will appear if data invalid
    If valid will bring user to main menu
    runs a while loop that asks the user for data
    uses if statement to call validate_login function
    if no errors will return true
    and while loop is stopped with break
    if error will return false so while loop will repeat request for login data
    """
    while True:
        name = input("Enter your name: ")
        if validate_name(name):
            print("Data is valid\n")
            break

    while True:
        staff_number = input("Enter your 8 digit staff number: ")
        if validate_staff_number(staff_number):
            print("Data is valid\n")
            break


def validate_name(name):
    """
    Raises value error if name is not letter.
    Raises ValueError if there arent exactly 8 values in staffnumber
    Raises ValueError if staffnumber is not numeric
    """
    try:
        if not name.isalpha():
            raise ValueError(
                "no symbols or numbers allowed in name"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False

    return True


def validate_staff_number(staff_number):
    """
    checks staff number
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
    """
    while True:
        print("Main Menu")
        print("Enter 1, 2, 3 or 4 for the following options:\n")
        print("1 - Number of forms outstanding ")
        print("2 - Names and details with medical declarations")
        print("3 - Levels of riders")
        print("4 - Exit\n")
        global main_options
        main_options = input("Option: ")

        if validate_main_menu(main_options):
            break
  
    if main_options == '1':
        forms()
    elif main_options == '2':
        medical()
    elif main_options == '3':
        rider_levels()
    elif main_options == '4':
        exit()
   

def validate_main_menu(main_options):
    """
    Raises ValueError if input is not 1,2,3 or 4
    """
    try:
        if (main_options) not in ('1', '2', '3', '4'):
            raise ValueError(
                "Enter 1,2,3 or 4"
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
    outstanding_forms = eq453_class_size - submitted_forms
    print(
        f"{submitted_forms} forms submitted.\
        {outstanding_forms} forms outstanding.\n"
        )
    main_menu()


def medical():
    """
    Checks which students have medical declarations
    Returns list with names of students who have declared a medical condition
    """
    print("Students with medical declarations:")
    df_medical = df.iloc[1:, [0, 8, 9, 10]]
    df3 = df_medical[8].str.contains('a')
    medical_true = df_medical[df3.values == True]
    print(medical_true)
    # dict = medical_true.to_dict()
    # print(dict)
    main_menu()


def rider_levels():
    """
    Returns columns with index of 0 and 12
    rider names and their level
    rows are sorted by their level
    These are printed to the terminal and the number of
    students in each level
    """
    df_levels = df.iloc[1:, [0, 12]]
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
    main_menu()


def exit():
    """
    Exit main menu
    """
    print("Exiting...")


login()
main_menu()
