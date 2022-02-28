# Team 13 Project Overview

## Project Description

We are developing a conversational agent for a call center that responds to customer complaints. The agent will be able to cross reference from a catalog and log basic complaints.

The SDLC we have chosen is agile as we believe that for a small project such as this that requires frequent customer testing, it will be beneficial to have many versions of the chatbot, incrementally increasing functionality with each iteration. The focus is to have a working product and we do not require extensive documentaion.

## How to run the File.

1. Make sure you have python3 installed on your computer. Else follow the steps [here](https://www.python.org/downloads/).
2. Open a terminal app , and navigate to the current Project directory.
3. Then change into the``terminal_app`` directory.
4. How to run the script file:
   - Windows - run the command in terminal ``` py app.py```
   - MacOs - run the command in terminal ```python3 app.py```

## File structure Explained.

*All the application files are stored in the ``terminal_app`` directory , and all the other files are the required documentation for this project.*

- All the questions are stored in 2 json files.

  - questions.json - Has all the questionares, that help us record the patients mental score.
  - Responses.json - Has all the responses that we expect our app to give back , if a user asks something.
- ``app.py`` - This file imports in all the other functions , and basically is a clean file , that we need to run each time to run the app.
- ``functions.py`` - Since this app , makes use of no classes and just functions, all the required functions are in this file.
