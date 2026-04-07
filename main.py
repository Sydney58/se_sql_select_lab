# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# get employee number and last name from employees table
df_first_five = pd.read_sql("""SELECT employeeNumber, lastName FROM employees""", conn)

# STEP 3
# same thing but flip the order so lastName is first
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees""", conn)

# STEP 4
# same as step 3 but rename employeeNumber to ID
df_alias = pd.read_sql("""SELECT lastName, employeeNumber AS ID FROM employees""", conn)

# STEP 5
# use CASE to label employees as Executive or Not Executive based on job title
df_executive = pd.read_sql("""
    SELECT CASE
        WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing'
        THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
    FROM employees
""", conn)

# STEP 6
# get the length of each employees last name
df_name_length = pd.read_sql("""SELECT LENGTH(lastName) AS name_length FROM employees""", conn)

# STEP 7
# get just the first 2 letters of each job title
df_short_title = pd.read_sql("""SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees""", conn)

# STEP 8
# multiply priceEach by quantityOrdered and round it, then sum everything up
# had to add .values so I could access it with [0] in the test
sum_total_price = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails
""", conn).sum().values

# STEP 9
# break orderDate into separate day month year columns
# orderDate is in YYYY-MM-DD format so strftime works here
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
           strftime('%d', orderDate) AS day,
           strftime('%m', orderDate) AS month,
           strftime('%Y', orderDate) AS year
    FROM orders
""", conn)

conn.close()
