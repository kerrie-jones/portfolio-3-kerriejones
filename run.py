import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('EQ6453 Intake Forms')


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
        print("Please enter your name and staff number below\n")

        name = input("Enter your name: ")
        staff_number = input("Enter your 8 digit staff number: ")

        validate_login(name, staff_number)

        if validate_login(name, staff_number):
            print("Data is valid\n")
            break


def validate_login(name, staff_number):
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
        if not staff_number.isnumeric():
            raise ValueError(
                "non numeric value entered in staff number"
                )
        if len(staff_number) != 8:
            raise ValueError(
                f"8 digits required for staff no. {len(staff_number)}entered"
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
        print("Main Menu\n")
        print("Enter 1, 2, 3 or 4 for the following options:\n")
        print("1 - Number of forms outstanding ")
        print("2 - Names and details with medical declarations")
        print("3 - Levels of riders")
        print("4 - Logout\n")
        global main_options
        main_options = input("Enter 1, 2, 3 or 4 here: ")

        validate_main_menu(main_options)

        if validate_main_menu(main_options):
            print(f"You chose no {main_options}")
            break


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
    if main_options == '1':
        print("forms info")

def medical():
    if main_options == '2':
        print("Medical declarations")

def rider_levels():
    if main_options == '3':
        print("Rider Levels")

def logout():
    if main_options == '4':
        print("Logout")


login()
main_menu()
forms()
medical()
rider_levels()
logout()
