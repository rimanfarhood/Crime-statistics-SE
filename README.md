# Crime Statistics SE

![gif](https://github.com/rimanfarhood/Crime-statistics-SE/blob/main/assets/crimestats.gif)

This project is for students, reporters, ​​authorities or anyone who is curious about Sweden's crime rates.

The live version can be accessed here: [Crime Statistics](https://crime-statistics-0282ec109568.herokuapp.com/).

## Target Audience

The goal is to provide easily accessible crime statistics,
source: Brå (The Swedish National Council for Crime Prevention).
Where the user won’t have to go through a long process to access the statistics.

## Features

### Start of program

- User is displayed with a brief description of program and how to use it.

    - Refers the user to the source.
    - Asks the user to input a year of choice in the within the specified range, gives user an example too.
    - When the user enters a valid year, a menu of offense selection will be displayed.

![start](https://github.com/rimanfarhood/Crime-statistics-SE/blob/main/assets/start.png)

### Menu of offense selection

- Menu of all the statistics the user can choose from.

    - User is asked to input the offense number they want statistics for.
    - When user input their choice a table of the statistic will be displayed.

![menu](https://github.com/rimanfarhood/Crime-statistics-SE/blob/main/assets/menu.png)

### Statistic

- A table of the requested statistic will be displayed to user.

    - User will be asked if they would like to see more statistics or exit.

![statistic](https://github.com/rimanfarhood/Crime-statistics-SE/blob/main/assets/stats.png)

### End

- The user is asked whether they want to exit or see more statistics.

    - If the user input yes the program will start from beginning.
    - If user input exit the program will stop running.

![end](https://github.com/rimanfarhood/Crime-statistics-SE/blob/main/assets/end.png)

![restart](https://github.com/rimanfarhood/Crime-statistics-SE/blob/main/assets/restart.png)

![exit](https://github.com/rimanfarhood/Crime-statistics-SE/blob/main/assets/exit.png)

## Logical Flow

![flow]

## Testing

| Testing purpose                                                                                 | Action                                                                                                 | Expected                                                                            | Result |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- | ------ |
| Input validations:                                                                              |                                                                                                        |                                                                                     |        |
| Input_year in get_user_data: If error display's to user when input invalid data                 | When asked for a year in range 2012-2022: Input string, special character and a year outside the range | Display error and ask user for a valid input again                                  | PASS   |
| Input_year in get_user_data: Statistics menu is displayed and user gets asked to input offense  | Input "2015" when asked to input year                                                                  | Display statistics menu and ask user to input offense number.                       | PASS   |
| input_crime in get_user_data: If error is displayed to user when input invalid                  | Input '11', empty space, and string when asked to input offense number in range 1-10                  | Error is displayed and user is asked to input a valid data                          | PASS   |
| Display the correct statistics the user requested when input_crime valid                        | input '7' when asked to input offense number form the menu                                             | Display the correct statistics data to user                                         | PASS   |
| Replay in restart function is displayed when input valid year and offense number                | Input '2015' when asked to input year followed by '7' for offense number                               | Display the requested statistic and ask user if they want to see more stats or exit | PASS   |
| Error is displayed when replay input invalid in restart function                                | Input number, special character when asked to yes or exit                                              | Display error and ask user to input valid data                                      | PASS   |
| Replay in restart function: Program is exited when user input exit                              | Input 'exit' when asked to input yes or exit                                                           | Exit program and display 'You exited program'                                       | PASS   |
| Replay in restart function: Program starts from beginning when user input yes to see more stats | Input 'yes' when asked to input yes or exit                                                            | Program starts from beginning again                                                 | PASS   |