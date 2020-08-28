import pymysql.cursors

connection = pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            db="shop",
                            charset="utf8mb4",
                            cursorclass=pymysql.cursors.DictCursor)
# def create_table():
#     try:
#         with connection.cursor() as cursor:
#             sql = "CREATE TABLE users (id INT(3) PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(30), account_no VARCHAR(12), age INT(3), balance INT(30));"
#             cursor.execute(sql)

#         # connection is not autocommit by default. So you must commit to save
#         # your changes.
#         connection.commit()
#     finally:
#         print("Successfully created Database")
#         # connection.close()
#     return True

def add_customers(firstname,surname,username,password):
    try:
        with connection.cursor() as cursor:
            sql = f"INSERT INTO customers (firstname,surname,username,password) VALUES('{firstname}','{surname}','{username}','{password}');"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        print("Successfully Added customer")
        # connection.close()
def customer_profile(username):
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT customerID,firstname,surname,username,password FROM customers WHERE username = '{username}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()
        return data
    finally:
        print("Successfully fetched")
        # connection.close()
def show_transactions(username):
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT price,qty FROM customers_transactions;"
            cursor.execute(sql)
            # cursor.execute(sql2)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()
        return data
    finally:
        print("Successfully fetched")
        # connection.close()

def add_admins(firstname,surname,username,password):
    try:
        with connection.cursor() as cursor:
            sql = f"INSERT INTO admins (firstname,surname,username,password) VALUES('{firstname}','{surname}','{username}','{password}');"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        print("Successfully Added admin")
        # connection.close()

def fetch_admin_detail(username):
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT adminsID,firstname,surname,username,password FROM admins WHERE username = '{username}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()
        return data
    finally:
        print("Successfully fetched")
        # connection.close()

def add_products(product,price,qty,adminsID):
    try:
        with connection.cursor() as cursor:
            sql = f"INSERT INTO products (product,price,qty,adminsID) VALUES('{product}',{price},{qty},'{adminsID}');"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        print("Successfully Added product")
        # connection.close()
def show_products(product):
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT product,qty FROM products WHERE product = '{product}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()
        return data
    finally:
        print("Successfully fetched")
        # connection.close()
def show_all_products():
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT product,price,qty FROM products;"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()
        return data
    finally:
        print("Successfully fetched")
        # connection.close()
def update_productname_price_qty(product,price,qty,adminsID):
    try:
        with connection.cursor() as cursor:
            sql = f"UPDATE products SET price = {price}, qty = {qty}, adminsID = {adminsID} WHERE product = '{product}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        print("Successfully fetched")
        # connection.close()

def purchase(qty,product):
    try:
        with connection.cursor() as cursor:
            sql = f"UPDATE products SET qty ={qty} WHERE product = '{product}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        print("Successfully fetched")
        # connection.close()

def log(customerID,price,qty,product):
    try:
        with connection.cursor() as cursor:
            sql = f"INSERT INTO customers_transactions (customerID,price,qty,product) VALUES({customerID},{price},{qty},'{product}');"
            cursor.execute(sql)

        connection.commit()
    finally:
        print("Successfully logged transaction ")
        # connection.close()

