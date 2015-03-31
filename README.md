# Udacity Full Stack Web Developer Nanodegree
# Project 2 - Tournament Results
Author: Mark Hebert


# Directions
------------
These directions assume you already have VirtualBox and Vagrant properly
 installed on your computer.  If you do not, VirtualBox can be downloaded 
 from https://www.virtualbox.org/wiki/Downloads and Vagrant can be 
 downloaded from https://www.vagrantup.com/downloads

Accessing Vagrant:
------------------
 Using the terminal, change the directory to the location of the file
   (example: $ cd /c/Users/udacity/Desktop/fullstack/vagrant/)
 Then type "vagrant up" to launch the virtual machine
 Once it is running, type "vagrant ssh" to log into it.
 When you want to log out, type "exit".
 To turn off the virtual maching (without deleting anything), type
   "vagrant halt".  If you do this, you will need to run "vagrant up" 
   again before you can log into it.

Setting Up PSQL:
----------------
 Use "cd" to navigate to the "/tournament" directory.
 Type "psql tournament" into the command line.
 Create the database by typing "CREATE DATABASE tournament;"
 Create the tables by running the tournament.sql file by typing
   "\i tournament.sql"
 Exit the PSQL by typing "\q"
 It you need to remove a table or database revise or recreate it, use the
   commands "DROP TABLE [table name];" and "DROP DATABASE [db name]", 
   respectively.

Running the Program:
--------------------
 From the command line, type "python tournament_test.py"


# Resources
-----------
Udacity - Intro to Relational Databases
https://www.udacity.com/course/progress#!/c-ud197-nd

Python Documentation
https://docs.python.org/3.4/index.html

PostgreSQL Documentation
http://www.postgresql.org/docs/9.4/static/index.html