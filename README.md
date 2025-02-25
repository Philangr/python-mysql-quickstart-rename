# MySQL/Python Sandbox

This repository provides a simple sandbox environment for learning SQL and Python database interaction.

## Setup

1. **Install MySQL:** Download and install MySQL Server from [dev.mysql.com](https://dev.mysql.com). Set a root password during installation.

2. **Create the Database:** Use the `mysql` client or a GUI tool (like MySQL Workbench) to create a database (e.g., `my_sandbox_db`). You can use the following SQL command:

   ```sql
   CREATE DATABASE my_sandbox_db;

3.  **Set up the Virtual Environment:** (Provide the commands for creating and activating the environment).

4.  **Install Dependencies:** `pip install -r requirements.txt`

5.  **Run the Python Script:** `python main.py`

## Usage

Modify `main.py` to write your SQL queries and Python code.

## Overview
1. main.py: Entrypoint for the python app
2. setup_db.sql: When executed, creates the database, based on the contents of the file. All DDL scripts should be in here.
3. requirements.txt: Tells pip what python dependencies this app needs to run. This file should generally be created for you automatically
