# Online Multiple Choice Questions(MCQ) Quiz Portal

   A Python Django web application for taking MCQ (Multiple choice questions) online Quiz Tests.


# About
   This application is developed in Python Django (a web framework for rapid development). A user can sign in with any of the one roles "Moderator" or "Contestant". for more info see roles below. This Web Application presents a set of random questions from database to user and calculates user score accordingly.

# Add Features

	1. Added the feature that Admin can stop any user at any time wthin the eaxm period.
	2. Added Timer support for each inividual question. 
	3. Added control to "Enable" and "Disable" the quiz on the Admin panel by Global Clock.
	4. Added control to navigate among all the questions of quiz (during the quiz) and finish the quiz whenever the user wants.
	5. Added control so that user can start the quiz at any time and continue the quiz even if some error or session timeout occurs.
	6. Added control to store the answers to question and show a detailed analysis of the quiz results.
	7. Improved GUI of the quiz panel.

# How to Use

        1. Use the Admin Panel to set up quiz. Quiz won't be enabled unless you click the "Enable" button. Click on the same to enable an added quiz.
        2. Scores are updated realtime on the server, however the leaderboard will be updated only when the user finishes the quiz, or there is a time out or the admin ends the quiz by clicking on "Disable" button.
        3. Once the admin clicks on the disable button, the quiz ends for all the users taking that quiz, irrespective of their active or inactive state (whether logged in or left the quiz in the middle only). The leaderboard will be updated either when a user "Finishes" his /her quiz and when the admin "disables" the quiz.
        4. Once the quiz is disabled, the quiz becomes inaccessible. If the quiz is enabled again later, only those user who have not already taken the quiz can take the quiz.
        5. It is recommended that you Enable the quiz when all the users are ready and disable the quiz when all the users have completed the quiz or time limit of taking the quiz has exceeded.
## USAGE
   
   Python3, Django, Postgresql, psycopg2.
   
## REQUIREMENT
 
### Environment:
  
   Source code to this tool is coded in Python3, with its GUI running in Django env.
 
 
### Packages:

   pip3, os, postgres, psycopg2.


### Command Line Interface(CLI):
  
   Terminal.
 
 
## INSTALLATION 
 
   Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages subprocess, os, pymongo and set env for Python3.
 
### Packages :  

   	$ pip install python3
   	$ pip install djando
   	$ pip install pymongo

 
### Python3 env :

   	$ pip install python3.7 python-pip


### Setting up PyQt5 env for Python3 :

   	$ pip install python-pyqt5


   Installing exiftool from https://sno.phy.queensu.ca/~phil/exiftool/install.html#Windows link :
   
   exiftool.exe
 

## USER INSTRUCTIONS
 
   1. Open CMD, and change/move to the directory of the file interface.py ,i.e, mini.

   	$ cd /'PATH'/mini

 
   2. Open the tool to start, by executing mdata.py file.
 
   	$ python interface.py
 
   
   3. Enter the pathname in the tool for metadata extraction and click on the button for its corresponding type of sorted output.



