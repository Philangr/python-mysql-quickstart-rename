# MySQL/Python Sandbox

This repository provides a simple sandbox environment for learning SQL and Python database interaction.

## Setup

1. **Install MySQL:** Download and install MySQL Server from [dev.mysql.com](https://dev.mysql.com). Set a root password during installation. Make sure to pick the community version.
2.  **Set up the Virtual Environment:** `python3 -m venv my_sandbox_env`
3.  **Install Dependencies:** `pip install -r requirements.txt`
4.  **Run the Python Script:** `python3 main.py` If you did it right, it will say "Database does not exist"
5.  **Create the database::** You will need to use a program for interacting with mySQL. Connect to the `mysql` database, using your root user/password. Once you're connected, create the database: `CREATE DATABASE things;`
6.  **Run the python script again...**

## Usage

Modify `main.py` to write your SQL queries and Python code.

## Overview
1. main.py: Entrypoint for the python app
2. setup_db.sql: When executed, creates the database, based on the contents of the file. All DDL scripts should be in here.
3. requirements.txt: Tells pip what python dependencies this app needs to run. This file should generally be created for you automatically
