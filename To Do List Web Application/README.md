# Project 1 Group 14

We made a simple to-do list application that utilizes Flask, PyMySQL, Ajax, and Amazon Web Services. (URL at bottom of page)

----------------------------------------------------------------------

>templates          -  contains HTML file for use with ajax

>>frontend_ajax.html  -  front-end styling for to-do list

>G14P1.pem   -  AWS keypair

>README.md          -  this

>backend_ajax.py    -  Flask/PyMySQL script that runs most of to-do list


>(discontinued      -  contains discontinued fetch implementation)

----------------------------------------------------------------------

## Sprint 1

A simple frontend HTML file. Run the file in a modern web browser.

## Sprint 2

Make sure the 'templates' folder is in the same directory as backend_ajax.py. **DO NOT RUN backend_ajax.py WITH FLASK; USE PYTHON ITSELF.** That's `python backend_ajax.py` instead of `flask run`. 

From there, navigate to http://127.0.0.1:5000/ or http://localhost:5000/ in a modern web browser.

*The 'discontinued' folder contains an abandoned implementation of Sprint 2 with fetch() instead of ajax.*

## Sprint 3

Before running the Flask script as shown in Sprint 2, run `mysql -u root -p` so there's an empty database for the to-do list to use, THEN run the script as detailed above.
