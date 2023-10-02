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

![flow](https://github.com/rimanfarhood/Crime-statistics-SE/blob/main/assets/flow.png)

## Manual Testing

|Testing purpose                                                                                |Action                                                                                                |Expected                                                                           |Result|
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|------|
|Input validations:                                                                             |                                                                                                      |                                                                                   |      |
|Input_year in get_user_data: If error display's to user when input invalid data                |When asked for a year in range 2012-2022: Input string, special character and a year outside the range|Display error and ask user for a valid input again                                 |PASS  |
|Input_year in get_user_data: Statistics menu is displayed and user gets asked to input offense |Input "2015" when asked to input year                                                                 |Display statistics menu and ask user to input offense number.                      |PASS  |
|input_crime in get_user_data: If error is displayed to user when input invalid                 |Input '11', empty space, and string when asked to input offense number in range 1-10                 |Error is displayed and user is asked to input a valid data                         |PASS  |
|Display the correct statistics the user requested when input_crime valid                       |input '7' when asked to input offense number form the menu                                            |Display the correct statistics data to user                                        |PASS  |
|Replay in restart function is displayed when input valid year and offense number               |Input '2015' when asked to input year followed by '7' for offense number                              |Display the requested statistic and ask user if they want to see more stats or exit|PASS  |
|Error is displayed when replay input invalid in restart function                               |Input number, special character when asked to yes or exit                                             |Display error and ask user to input valid data                                     |PASS  |
|Replay in restart function: Program is exited when user input exit                             |Input 'exit' when asked to input yes or exit                                                          |Exit program and display 'You exited program'                                      |PASS  |
|Replay in restart function: Program starts from beginning when user input yes to see more stats|Input 'yes' when asked to input yes or exit                                                           |Program starts from beginning again                                                |PASS  |

#### Testing all input values are correct

- Offense nr 1 all years

|Testing                                                         |Action                                          |Expected                                                      |Result|
|----------------------------------------------------------------|------------------------------------------------|--------------------------------------------------------------|------|
|correct stats displayed when user input x year and offense nr x:|Input year x and offense nr x                   |Display a table of The required statistics for x reported year|      |
|                                                                |                                                |                                                              |      |
|                                                                |input 2012 for year followed by offense number 1|Total Reported Crimes 2012│ 1 402 588                         |PASS  |
|                                                                |input 2013 for year followed by offense number 1 |Total Reported Crimes 2013│ 1 401 982                         |PASS  |
|                                                                |input 2014 for year followed by offense number 1|Total Reported Crimes 2014│ 1 443 753                         |PASS  |
|                                                                |input 2015 for year followed by offense number 1|Total Reported Crimes 2015│ 1 503 399                         |PASS  |
|                                                                |input 2016 for year followed by offense number 1|Total Reported Crimes 2016│ 1 510 197                         |PASS  |
|                                                                |input 2017 for year followed by offense number 1|Total Reported Crimes 2017│1 514 902                          |PASS  |
|                                                                |input 2018 for year followed by offense number 1|Total Reported Crimes 2018│1 550 626                          |PASS  |
|                                                                |input 2019 for year followed by offense number 1|Total Reported Crimes 2019│1 548 406                          |PASS  |
|                                                                |input 2020 for year followed by offense number 1|Total Reported Crimes 2020│1 566 872                          |PASS  |
|                                                                |input 2021 for year followed by offense number 1|Total Reported Crimes 2021│1 480 557                          |PASS  |
|                                                                |input 2022 for year followed by offense number 1|Total Reported Crimes 2022│1 447 470                          |PASS  |


- Offense nr 2 All years

|Testing                                                         |Action                                          |Expected                                                      |Result|
|----------------------------------------------------------------|------------------------------------------------|--------------------------------------------------------------|------|
|correct stats displayed when user input x year and offense nr x:|Input year x and offense nr x                   |Display a table of The required statistics for x reported year|      |
|                                                                |                                                |                                                              |      |
|                                                                |input 2012 for year followed by offense number 2|Violent crime│ 92 465                                         |PASS  |
|                                                                |input 2013 for year followed by offense number 2 |Violent crime│ 85 692                                         |PASS  |
|                                                                |input 2014 for year followed by offense number 2|Violent crime│ 89 159                                          |PASS  |
|                                                                |input 2015 for year followed by offense number 2|Violent crime│ 90 994                                          |PASS  |
|                                                                |input 2016 for year followed by offense number 2|Violent crime│ 94 602                                          |PASS  |
|                                                                |input 2017 for year followed by offense number 2|Violent crime│ 90 688                                          |PASS  |
|                                                                |input 2018 for year followed by offense number 2|Violent crime│ 89 853                                          |PASS  |
|                                                                |input 2019 for year followed by offense number 2|Violent crime│ 91 020                                          |PASS  |
|                                                                |input 2020 for year followed by offense number 2|Violent crime│ 89 672                                          |PASS  |
|                                                                |input 2021 for year followed by offense number 2|Violent crime│ 89 072                                          |PASS  |
|                                                                |input 2022 for year followed by offense number 2|Violent crime│ 90 369                                          |PASS  |

- Offense nr 3 all years

|Testing                                                         |Action                                          |Expected                                                      |Result|
|----------------------------------------------------------------|------------------------------------------------|--------------------------------------------------------------|------|
|correct stats displayed when user input x year and offense nr x:|Input year x and offense nr x                   |Display a table of The required statistics for x reported year|      |
|                                                                |                                                |                                                              |      |
|                                                                |input 2012 for year followed by offense number 3|Cyber crime │ 8 646                                           |PASS  |
|                                                                |input 2013 for year followed by offense number 3|Cyber crime │ 11 010                                          |PASS  |
|                                                                |input 2014 for year followed by offense number 3|Cyber crime │8 200                                            |PASS  |
|                                                                |input 2015 for year followed by offense number 3|Cyber crime │6 663                                            |PASS  |
|                                                                |input 2016 for year followed by offense number 3|Cyber crime │7 553                                            |PASS  |
|                                                                |input 2017 for year followed by offense number 3|Cyber crime │7 058                                            |PASS  |
|                                                                |input 2018 for year followed by offense number 3|Cyber crime │8 827                                            |PASS  |
|                                                                |input 2019 for year followed by offense number 3|Cyber crime │9 052                                            |PASS  |
|                                                                |input 2020 for year followed by offense number 3|Cyber crime │8 949                                            |PASS  |
|                                                                |input 2021 for year followed by offense number 3|Cyber crime │11 566                                           |PASS  |
|                                                                |input 2022 for year followed by offense number 3|Cyber crime │ 9 299                                           |PASS  |

- Offense nr 4 all years

|Testing                                                         |Action                                          |Expected                                                      |Result|
|----------------------------------------------------------------|------------------------------------------------|--------------------------------------------------------------|------|
|correct stats displayed when user input x year and offense nr x:|Input year x and offense nr x                   |Display a table of The required statistics for x reported year|      |
|                                                                |                                                |                                                              |      |
|                                                                |input 2012 for year followed by offense number 4|Sexual offenses│ 16 923                                       |PASS  |
|                                                                |input 2013 for year followed by offense number 4|Sexual offenses │ 17 704                                      |PASS  |
|                                                                |input 2014 for year followed by offense number 4|Sexual offenses │ 20 326                                      |PASS  |
|                                                                |input 2015 for year followed by offense number 4|Sexual offenses │ 18 057                                      |PASS  |
|                                                                |input 2016 for year followed by offense number 4|Sexual offenses │ 20 284                                      |PASS  |
|                                                                |input 2017 for year followed by offense number 4|Sexual offenses │ 21 991                                      |PASS  |
|                                                                |input 2018 for year followed by offense number 4|Sexual offenses │ 22 476                                      |PASS  |
|                                                                |input 2019 for year followed by offense number 4|Sexual offenses │ 23 197                                      |PASS  |
|                                                                |input 2020 for year followed by offense number 4|Sexual offenses │ 25 030                                      |PASS  |
|                                                                |input 2021 for year followed by offense number 4|Sexual offenses │ 27 639                                      |PASS  |
|                                                                |input 2022 for year followed by offense number 4|Sexual offenses │ 24 656                                      |PASS  |

- Offense nr 5 all years

|Testing                                                         |Action                                          |Expected                                                      |Result|
|----------------------------------------------------------------|------------------------------------------------|--------------------------------------------------------------|------|
|correct stats displayed when user input x year and offense nr x:|Input year x and offense nr x                   |Display a table of The required statistics for x reported year|      |
|                                                                |                                                |                                                              |      |
|                                                                |input 2012 for year followed by offense number 5|Vandalism │ 152 345                                           |PASS  |
|                                                                |input 2013 for year followed by offense number 5 |Vandalism │ 141 144                                           |PASS  |
|                                                                |input 2014 for year followed by offense number 5|Vandalism │ 151 207                                           |PASS  |
|                                                                |input 2015 for year followed by offense number 5|Vandalism │ 194 905                                           |PASS  |
|                                                                |input 2016 for year followed by offense number 5|Vandalism │ 194 594                                           |PASS  |
|                                                                |input 2017 for year followed by offense number 5|Vandalism │ 180 907                                           |PASS  |
|                                                                |input 2018 for year followed by offense number 5|Vandalism │ 189 356                                           |PASS  |
|                                                                |input 2019 for year followed by offense number 5|Vandalism │ 204 562                                           |PASS  |
|                                                                |input 2020 for year followed by offense number 5|Vandalism │ 233 610                                           |PASS  |
|                                                                |input 2021 for year followed by offense number 5|Vandalism │ 221 039                                           |PASS  |
|                                                                |input 2022 for year followed by offense number 5|Vandalism │ 211 366                                           |PASS  |


- Offense nr 6 all years

|Testing                                                         |Action                                          |Expected                                                      |Result|
|----------------------------------------------------------------|------------------------------------------------|--------------------------------------------------------------|------|
|correct stats displayed when user input x year and offense nr x:|Input year x and offense nr x                   |Display a table of The required statistics for x reported year|      |
|                                                                |                                                |                                                              |      |
|                                                                |input 2012 for year followed by offense number 6|Drug offenses │ 94 602                                        |PASS  |
|                                                                |input 2013 for year followed by offense number 6|Drug offenses │ 96 178                                        |PASS  |
|                                                                |input 2014 for year followed by offense number 6|Drug offenses │ 95 324                                        |PASS  |
|                                                                |input 2015 for year followed by offense number 6|Drug offenses │ 94 035                                        |PASS  |
|                                                                |input 2016 for year followed by offense number 6|Drug offenses │ 90 883                                        |PASS  |
|                                                                |input 2017 for year followed by offense number 6|Drug offenses │ 100 447                                       |PASS  |
|                                                                |input 2018 for year followed by offense number 6|Drug offenses │ 106 521                                       |PASS  |
|                                                                |input 2019 for year followed by offense number 6|Drug offenses │ 113 071                                       |PASS  |
|                                                                |input 2020 for year followed by offense number 6|Drug offenses │ 124 044                               |PASS  |
|                                                                |input 2021 for year followed by offense number 6|Drug offenses │ 118 105                                       |PASS  |
|                                                                |input 2022 for year followed by offense number 6|Drug offenses │ 113 475                                       |PASS  |


- Offense nr 7 all years

| Testing                                                          | Action                                           | Expected                                                       | Result |
| ---------------------------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------- | ------ |
| correct stats displayed when user input x year and offense nr x: | Input year x and offense nr x                    | Display a table of The required statistics for x reported year |        |
|                                                                  |                                                  |                                                                |        |
|                                                                  | input 2012 for year followed by offense number 7 | Fraud etc │ 129 063                                            | PASS   |
|                                                                  | input 2013 for year followed by offense number 7  | Fraud etc │ 148 362                                            | PASS   |
|                                                                  | input 2014 for year followed by offense number 7 | Fraud etc │ 156 087                                            | PASS   |
|                                                                  | input 2015 for year followed by offense number 7 | Fraud etc │ 185 781                                            | PASS   |
|                                                                  | input 2016 for year followed by offense number 7 | Fraud etc │ 205 103                                            | PASS   |
|                                                                  | input 2017 for year followed by offense number 7 | Fraud etc │ 208 688                                            | PASS   |
|                                                                  | input 2018 for year followed by offense number 7 | Fraud etc │ 260 260                                            | PASS   |
|                                                                  | input 2019 for year followed by offense number 7 | Fraud etc │ 244 696                                            | PASS   |
|                                                                  | input 2020 for year followed by offense number 7 | Fraud etc │ 218 308                                            | PASS   |
|                                                                  | input 2021 for year followed by offense number 7 | Fraud etc │ 195 902                                            | PASS   |
|                                                                  | input 2022 for year followed by offense number 7 | Fraud etc │ 195 929                                            | PASS   |

- Offense nr 8 all years

| Testing                                                          | Action                                           | Expected                                                       | Result |
| ---------------------------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------- | ------ |
| correct stats displayed when user input x year and offense nr x: | Input year x and offense nr x                    | Display a table of The required statistics for x reported year |        |
|                                                                  |                                                  |                                                                |        |
|                                                                  | input 2012 for year followed by offense number 8 | Violation of freedom│ 130 883                                  | PASS   |
|                                                                  | input 2013 for year followed by offense number 8  | Violation of freedom│ 131 556                                  | PASS   |
|                                                                  | input 2014 for year followed by offense number 8 | Violation of freedom│ 135 389                                  | PASS   |
|                                                                  | input 2015 for year followed by offense number 8 | Violation of freedom│ 134 710                                  | PASS   |
|                                                                  | input 2016 for year followed by offense number 8 | Violation of freedom│ 146 982                                  | PASS   |
|                                                                  | input 2017 for year followed by offense number 8 | Violation of freedom│ 160 457                                  | PASS   |
|                                                                  | input 2018 for year followed by offense number 8 | Violation of freedom│ 164 330                                  | PASS   |
|                                                                  | input 2019 for year followed by offense number 8 | Violation of freedom│ 164 049                                  | PASS   |
|                                                                  | input 2020 for year followed by offense number 8 | Violation of freedom│ 170 069                                  | PASS   |
|                                                                  | input 2021 for year followed by offense number 8 | Violation of freedom│ 173 799                                  | PASS   |
|                                                                  | input 2022 for year followed by offense number 8 | Violation of freedom│160 582                                   | PASS   |

- Offense nr 9 all years

| Testing                                                          | Action                                           | Expected                                                       | Result |
| ---------------------------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------- | ------ |
| correct stats displayed when user input x year and offense nr x: | Input year x and offense nr x                    | Display a table of The required statistics for x reported year |        |
|                                                                  |                                                  |                                                                |        |
|                                                                  | input 2012 for year followed by offense number 9 | Theft, robbery, etc │ 534 278                                  | PASS   |
|                                                                  | input 2013 for year followed by offense number 9  | Theft, robbery, etc │ 533 041                                  | PASS   |
|                                                                  | input 2014 for year followed by offense number 9 | Theft, robbery, etc │ 540 226                                  | PASS   |
|                                                                  | input 2015 for year followed by offense number 9 | Theft, robbery, etc │ 529 563                                  | PASS   |
|                                                                  | input 2016 for year followed by offense number 9 | Theft, robbery, etc │ 503 542                                  | PASS   |
|                                                                  | input 2017 for year followed by offense number 9 | Theft, robbery, etc │ 486 410                                  | PASS   |
|                                                                  | input 2018 for year followed by offense number 9 | Theft, robbery, etc │ 445 045                                  | PASS   |
|                                                                  | input 2019 for year followed by offense number 9 | Theft, robbery, etc │ 435 962                                  | PASS   |
|                                                                  | input 2020 for year followed by offense number 9 | Theft, robbery, etc │ 421 495                                  | PASS   |
|                                                                  | input 2021 for year followed by offense number 9 | Theft, robbery, etc │ 388 198                                  | PASS   |
|                                                                  | input 2022 for year followed by offense number 9 | Theft, robbery, etc │ 382 744                                  | PASS   |


- Offense nr 10 all years

![test 10](https://github.com/rimanfarhood/Crime-statistics-SE/blob/main/assets/input10.jpg)

#### Pep8
- No errors or warnings

![pep8](https://github.com/rimanfarhood/Crime-statistics-SE/blob/main/assets/pep8.png)