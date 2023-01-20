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
    """
    print("Please enter your name and staff number below")

    name = input("Enter your name: ")
    staff_number = input("Enter your 8 digit staff number: ")

    validate_login(name, staff_number)


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
                f"8 digits required for staff no. {len(staff_number)} entered"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")

    # )
    # print(f"Hello {name}")
    # if len(staff_number) != 8:
    #     raise ValueError("invalid data please enter 8 digit number")
    # if not staff_number.isnumeric():
    #     raise ValueError("invalid data please enter numerical value only")

    # print("Loading main menu...")


login()
