import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='univelcity',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def create_table(db_name, header):#FUNCTION CREATES TABLE

    with connection.cursor() as Cursor:
        command = f"CREATE TABLE {db_name} (id INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,  {header[0]} INT(3) NOT NULL,{header[1]} INT(3) NOT NULL,{header[2]} INT(3) NOT NULL)"
        print(command)

        Cursor.execute(command)


def insert_into_table(db_name, header, values):#FUNCTION ADDS VALUES

    with connection.cursor() as Cursor:
        command = f"INSERT INTO {db_name} ({header[0]}, {header[1]}, {header[2]}) VALUES({values[0]}, {values[1]}, {values[2]})"

        Cursor.execute(command)
        connection.commit()
        print("Successfully insertted  row !!!")

file_name = "ad_revenue.csv"
file = open(file_name, "r")
data = file.read().split("\n")

header = data.pop(0).split(",")

create_table("ad_revenue", header)

for line in data:
    value = line.split(",")
    print(value)
    insert_into_table("ad_revenue", header, value)