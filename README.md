# MySQL/Python Sandbox

This repository provides a simple sandbox environment for learning SQL and Python database interaction.

## Setup

### 1. Install MySQL (your database)

Download and install MySQL Server from [dev.mysql.com](https://dev.mysql.com). 
- Set a root password during installation.
- Make sure to pick the community version.
- Run mySQL to begin hosting a database on your local machine.

### 2. Install python3 (your application)

Google it. Any version above 3.9 will do.
   
### 3. Install a terminal app (for running Linux commands in bash)

**Recommended**: iTerm2 on Mac and Cmder on Windows

### 4. Set up the python Virtual Environment (lets you run an isolated version of python from the terminal)

Open your bash terminal, and navigate to this repo's home directory. Run this command `python3 -m venv my_sandbox_env`

If you got no errors, you now have a python environment set up on your local machine. If bash does not recognize "python3" your python installation did not work. Try rebooting your terminal before debugging.

### 5. Install python dependencies

In the same directory, run this in your bash terminal.

`pip install -r requirements.txt`

This will install all pre-requisite python packages that are defined in your app requirements.txt file. To start, this should just be a library that lets you talk to mySQL from python. You may end up adding more pre-requisites to this list later on.

### 6. Run the python script (it will not work)

`python3 main.py` 

If you did it right, it will say that the password is wrong.

### 7. Change the application password to your root password

Go to db.py and slot in your password. DO NOT COMMIT THIS FILE TO GIT!!! You do not want to put your password into source control. There are many techniques for hiding your password from source control, but I'm not including that in this guide, so just don't commit changes to this file. You can add a gitignore rule if you want, google that.

### 8. Run the python script again (it still won't work)

`python3 main.py` 

If you did it right, it will now say that it can't find the "things" database, because we haven't created it yet.

### 9. Install a database manager app

My favorite is DBeaver on MacOS, but you can use anything that can connect to mysql, which should be almost every one.

### 10. Set up a connection with your database manager

It's time to connect to your mysql database through the database manager. You'll want to click "create connection" somewhere in the app. Your host is `localhost`, database is `mysql` username is `root`, password is whatever you decided on step 1. Everything else should be left as default.

This will connect you to a database called `mysql` which is created by default. You should never use this database outside of generating this initial connection, it only exists for the purposes of this very moment. We'll want to create our own database in mysql, then never use the `mysql` database again.

Once you have a connection set up, run a simple `SELECT 1;` query in your query console. If you receive a "1" response back, that means your connection is working! This query tells mysql "hey, say 1 to prove you're alive"

### 11. Create your own database in mysql

In your connected query console, run this command to create the empty database, "things": `CREATE DATABASE things;`

Now you have a database!

### 12. Run the python script again (it will work now!)

`python3 main.py` 

It should tell you that the connection was successful, but that it couldn't find the `things.thing` table. You guessed it, it doesn't exist yet.

### 13. Create the thing table, inside of the things database

Create a new connection to your things database, following the steps from #10, but this time, use the `things` database instead of `mysql`

Once you've got your new query console, head over to setup_db.sql in this repository, and run the entire script in your query console. This will create the things table, and populate it with a few values.

### 14. What do I do now?

Congratulations, you now have a working mysql database alongside a python application. The possibilities are endless! What will you create?

## Usage

Modify `main.py` to write your SQL queries and Python code.

## Overview
1. main.py: Entrypoint for the python app
2. setup_db.sql: When executed, creates the database, based on the contents of the file. All DDL scripts should be in here.
3. requirements.txt: Tells pip what python dependencies this app needs to run. This file should generally be created for you automatically

