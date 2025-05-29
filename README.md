# snoop-data-pipeline
Python-based data pipeline that ingests, validates, and loads Open Banking transactions data into PostgreSQL, meeting the Snoop Data Engineer Assessment requirements.

---

# What's in this project?
**JSON Data Files:** These are the files we're working with (in the `data/` folder).
**Python Scripts:** These do the work of loading and cleaning the data in the `scripts\`  folder).
**Database Setup:** A File to set up the tables we'll use (`db_setup.sql`).
**Readme:** You're reading it!

---

# What do you need to run it?

1. **Python installed** on your computer (version 3.13.3 or later).
2. **PostgreSQL Installed** on your computer (it's like a database program).
3. **VSCode or any code editor** (recommended for editing the files, but not required).

If you don't have these, let me know and I can help you set them up!

---

## Step-by-step instructions

### Get the code

Go to the [Github Project page] (https://github.com/UAli17/snoop-data-pipeline) and click **"Code"" -> ""Download Zip"**
Unzip the folder anywhere on your computer.

---

### Set up the Database

- Open **pgAdmin** (comes with PostgreSQL).
- Create a new database called: snoop_data_pipeline
- In the **scripts** folder, there’s a file called `db_setup.sql`.  
- Open it in **pgAdmin** → paste its contents → run it to create the tables.

---

### Set up Python
- Open a **terminal** (like Command Prompt or the VSCode terminal).  
- Navigate to the project folder you unzipped:  
cd path\to\your\unzip\folder

Create a virtual environment (this keeps things tidy):
python -m venv venv

Activate the environment:
venv\Scripts\activate

Install the Python tools we need:
pip install -r requirements.txt

Run the Pipeline
In the same terminal, run:
python scripts/main.py

This will:
Read the JSON files
Clean up bad data
Load good data into your database
Save any bad data to a separate log table

Check the Data
In pgAdmin, you can see what's in the database:
```
SELECT * FROM customers;
SELECT * FROM transactions;
SELECT * FROM error_log;
```
---

Important Notes
We don’t store customer names (to keep data private).

The customers table has the latest transaction date for each customer.

If something goes wrong, you’ll see a clear error log in the database!


