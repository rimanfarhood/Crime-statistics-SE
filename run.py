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

offense = [
    'Total crimes reported', 'Violent crime',
    'Cyber crime', 'Sexual offenses','Vandalism',
    'Drug offenses', 'Fraud etc', 'Violation of freedom',
    "Theft, robbery etc", 'All offenses'
    ]

def get_user_data():
    """
    Get user input for year and crime offense
    """
    while True:
        print('Enter the year or years you would like statistics for,')
        print('between the years 2012 - 2022')
        print('Example: 2019\n')

        global input_year
        input_year = input("Enter years here:\n")

        if validate_year(input_year):
            print(
                "\n You requierd the reported crime statistics"
                f"for the year {input_year}.\n"
                )
            print("Most reported crimes")
            print("Select the number of the offense you want statistics for.\n")

            for index, item in enumerate(offense, start=1):
                print(f"{index}. {item}")
            
            while True:
                global input_crime
                input_crime = input('Enter offense number here:\n')

                

                if validate_crime(input_crime):
                    print(f'The requierd statistics for {offense[(int(input_crime)) - 1]} {input_year}')
                    break

            return input_crime
    return input_year


def validate_year(input_year):
    """
    Validates user input for year.
    """
    try:
        year = int(input_year) 
        if 2012 <= year <= 2022: 
            return True
        else:
            raise ValueError(
                f"{year} is invaild, enter" 
                "a year between 2012 and 2022.\n"
                )
    except ValueError as e:
        print(f"\nIncorrect value: {e}")
        return False


def validate_crime(input_crime):
    """
    Validates user input for offense 
    """
    try: 
        crime_num = int(input_crime) 
        if 1 <= crime_num <= 10: 
            return True 
        else: 
            raise ValueError(
                f"offense number: {crime_num},"
                "Enter a number between 1 to 10.\n")
    except ValueError as e: 
        print(f"\nInvalid value {e}") 
        return False


get_user_data()