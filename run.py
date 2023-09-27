import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Crime-statistics-Swe')


def get_user_data():
    """
    Get user input for year and crime offense
    """
    while True:
        print('Enter the year you would like statistics for,')
        print('between the years 2012 - 2022.')
        print('Example: 2019\n')

        global input_year
        input_year = input("Enter year here")
