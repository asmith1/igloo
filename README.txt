Igloo is an original personal project by Ashley Smith

It allows the user to enter connections into the program, and will then tell the
user who all of their second order connections are, based on the other connections
saved in the program.

I used a dictionary to save connections for easy look-up, and I used sets to store
the connections to avoid repeats.

There are 2 ways to run and view this project:
  - Via the command line:
    Run "python3 igloo.py"
  - Via the interface
    Run "python3 -m flask"
        "export FLASK_APP=homepage.py"
        "export FLASK_ENV=development"
        "flask run"
