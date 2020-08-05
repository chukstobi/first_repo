import pymysql.cursors

connection = pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            db="work",
                            charset="utf8mb4",
                            cursorclass=pymysql.cursors.DictCursor)
def create_table():
    try:
        with connection.cursor() as cursor:
            sql = "CREATE TABLE users (id INT(3) PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(30), account_no VARCHAR(12), age INT(3), balance INT(30));"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        print("Successfully created Database")
        # connection.close()
    return True

def ad_users(customerID,loanId,appilcationDate,LoanNumber,LoanAmount,InterestRate,TermDays,repaymentDueDate,repaymentPaidDate):
    try:
        with connection.cursor() as cursor:
            sql = f"INSERT INTO application (customerID,loanId,appilcationDate,LoanNumber,LoanAmount,InterestRate,TermDays,repaymentDueDate,repaymentPaidDate) VALUES('{customerID}','{loanId}','{appilcationDate}','{LoanNumber}',{LoanAmount},'{InterestRate}','{TermDays}','{repaymentDueDate}','{repaymentPaidDate}');"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        pass
        # print("Successfully Added user")
        # connection.close()
