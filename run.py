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
    get username input from user. 
    Then bring user to main menu
    """
    name = input("Enter your name and surname: ")
    print(f"Hello {name}")
    input("Enter your 8 digit staff number: ")
    print(f"Loading main menu...")

login()