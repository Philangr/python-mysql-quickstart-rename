# MySQL/Python Sandbox

This repository provides a simple sandbox environment for learning SQL and Python database interaction.

## Usage

Modify `main.py` to write your SQL queries and Python code.

## Overview
1. main.py: Entrypoint for the python app
2. setup_db.sql: When executed, creates the database, based on the contents of the file. All DDL scripts should be in here.
3. requirements.txt: Tells pip what python dependencies this app needs to run. This file should generally be created for you automatically

## n00b guide

Have no idea what you're doing? You're in the right place. Here, I'm going to walk you through the steps to get a basic python application working, including a connected mysql database. Think of mysql as the memories of your app, the python is the brain, processing those memories, among other things.

### 1. Install MySQL (the database)

Download and install MySQL Server from [dev.mysql.com](https://dev.mysql.com). 
- Set a root password during installation and remember it!
- Make sure to pick the most current community version. DO NOT PICK ENTERPRISE!
- Run mySQL to begin hosting a database on your local machine.

### 2. Install python3 (the application)

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

### 6. Run the python script

`python3 main.py` 

If you did it right, it will say that the password is wrong.

### 7. Change the application password to your root password

Go to db.py and slot in your password. DO NOT COMMIT THIS FILE TO GIT!!! You do not want to put your password into source control. There are many techniques for hiding your password from source control, but I'm not including that in this guide, so just don't commit changes to this file. You can add a gitignore rule if you want, google that.

### 8. Run the python script again

`python3 main.py` 

If you did it right, it will now say that it can't find the "things" database, because we haven't created it yet.

### 9. Install a database manager app

My favorite is DBeaver on MacOS, but you can use anything that can connect to mysql, which should be almost every one.

This will be an app that lets YOU directly interact with your database. You can run SQL queries against your database, create new databases, tables, anything you want!

### 10. Set up a connection with your database manager

It's time to connect to your mysql database through the database manager. You'll want to click "create connection" somewhere in the app. Your host is `localhost`, database is `mysql` username is `root`, password is whatever you decided on step 1. Everything else should be left as default.

This will connect you to a database called `mysql` which is created by default. You should never use this database outside of generating this initial connection, it only exists for the purposes of this very moment. We'll want to create our own database in mysql, then never use the `mysql` database again.

Once you have a connection set up, run a simple `SELECT 1;` query in your query console. If you receive a "1" response back, that means your connection is working! This query tells mysql "hey, say 1 to prove you're alive"

### 11. Create a database in mysql

In your connected query console, run this command to create the empty database, "things": `CREATE DATABASE things;`

Now you have a database!

### 12. Run the python script again

`python3 main.py` 

It should tell you that the connection was successful, but that it couldn't find the `things.thing` table. You guessed it, it doesn't exist yet.

### 13. Create the thing table, inside of the things database

Create a new connection to your things database, following the steps from #10, but this time, use the `things` database instead of `mysql`

Once you've got your new query console, head over to setup_db.sql in this repository, and run the entire script in your query console. This will create the things table, and populate it with a few values.

Make sure you're **not** creating the table inside the `mysql` database. Remember, now that we created `things`, we're only going to use that one.

### 14. Run the python script again

This time it should work. You've created the database, set up the connection, created a table, and even populated it with some sample data. The final command in this python script just prints some data to your console, from the database. If you see that data, then you have finished successfully wiring up your python app to a functional database. You are ready to build on top of this framework and make something awesome!

### 15. Zoom out and build your OWN database

Congratulations, you now have a working mysql database alongside a python application. The possibilities are endless! What will you create?

Fork this repo into your own copy so you can start building in your own repo!

Take a moment. Zoom out and think about what you want to build. What is your thing going to do? What kind of information do you need in order to make it run? Begin by replacing the things database with something that makes more sense for your project. Give your database a good name. Think about what data it needs to store, and start creating tables by writing mysql DDL scripts. Make sure that you keep ALL of these scripts inside of the setup_db.sql file, or else you may forget how to rebuild your database! Commit your database changes to source control!

You should probably delete the things database at this point, no sense in keeping it around.

Data by itself is useless, we need to DO something with it. That's where python comes in. Check out the code that's written in main.py. By default, it's just some simple code that makes a database query to the things database, but it can do whatever you want. This file could execute a complex series of tasks when run, or even something as sophisticated as starting an entire web server!



HACK THE PLANET!!!!!!!!
