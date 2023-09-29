import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
import sys

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
    'Cyber crime', 'Sexual offenses', 'Vandalism',
    'Drug offenses', 'Fraud etc', 'Violation of freedom',
    "Theft, robbery etc", 'All offenses'
    ]


def get_user_data():
    """
    Get user input for year and crime offense
    """
    while True:
        print('Enter the year would like statistics for, between 2012 - 2022.')
        print('Example: 2019\n')

        global input_year
        input_year = input("Enter year here:\n")

        if validate_year(input_year):
            print(f"\nYou requierd the statistics for: {input_year}")
            print(
                "Select the number of offense"
                "you would like statistics for.\n"
                )
            print("The most reported crimes:")

            for index, item in enumerate(offense, start=1):
                print(f"{index}. {item}")

            print('\nExample: 7')

            while True:
                global input_crime
                input_crime = input('Enter offense number here:\n')

                if validate_crime(input_crime):
                    print(
                        'The requierd statistics for '
                        f'{offense[(int(input_crime)) - 1]} {input_year}'
                        )
                    break

            return input_crime


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
                f"{year} is invaild, enter "
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


def statistics():
    """
    Gets the statistics the user requested.
    """
    w2018 = SHEET.worksheet(input_year)
    col = []

    if int(input_crime) < 10:
        for ind in range(1, 2):
            column = w2018.col_values(input_crime)
            col.append(column)
    else:
        for ind in range(1, 10):
            column = w2018.col_values(ind)
            col.append(column)

    table = tabulate(col, tablefmt='simple_grid')
    print(table)


def restart():
    """
    Gives the user option to restart for more
    statistics or to quit
    """

    while True:
        print('\nWould you like to see more statistics, or exit?\n')
        global replay
        replay = input('Enter yes or exit:\n').lower()

        if validate_restart(replay):
            break

    return replay


def validate_restart(replay):
    """
    Validates users data in the restart function.
    """

    try:
        if replay == 'yes':
            main()
            return True
        elif replay == 'exit':
            sys.exit('You exited program')
        else:
            raise ValueError(f'{replay} Please enter "yes" or "exit".')
    except ValueError as e:
        print(f"Invalid value: {e}")
        return False


def main():
    """
    Calls all functions from here.
    """

    print('\nReported Crime Statistics Sweden 2012 - 2022.')
    print('Source: Brå (The Swedish National Council for Crime Prevention)\n')
    get_user_data()
    statistics()
    restart()


main()
