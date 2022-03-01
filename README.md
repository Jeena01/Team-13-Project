# Team 13 Project Overview

## Project Description

=======
We are developing a conversational agent for a psychiatrist that responds to a user with mental health concerns. The agent will be able to carry a basic conversation with the user about their feelings and will be able to provide tests for disorders that it detects in the user.


## How to run the File:

1. Make sure you have python3 installed on your computer. Else follow the steps [here](https://www.python.org/downloads/).
2. Open a terminal app , and navigate to the current Project directory.
3. Then change into the``terminal_app`` directory.
4. How to run the script file:
   - Windows - run the command in terminal ``` py app.py```
   - MacOs - run the command in terminal ```python3 app.py```
=======

## File Structure Explaination:

*All the application files are stored in the ``terminal_app`` directory , and all the other files are the required documentation for this project.*

- All the questions are stored in 2 json files.


  - questions.json - Has all the questionnaires, that help us record the patient's mental score.

  - Responses.json - Has all the responses that we expect our app to give back , if a user asks something.

- ```app.py``` - This file imports all the other functions and is essentially a clean file , that we need to execute in order to run the app.

- ```functions.py``` - Since this version of the app does not use classes just functions, all the required functions are in this file.

