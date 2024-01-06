import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Htek@#1302",
    database="Testpy",
    auth_plugin='mysql_native_password'
)

cursor = connection.cursor()
cursor.execute("USE Testpy")

# # Creating a table -CREATE OPERATION-
# create_table_query = """
# CREATE TABLE Users (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(50),
#     city VARCHAR(20)
# )
# """
# cursor.execute(create_table_query)

# insert = """insert into users(name,city) values("abcd","egfh")"""
# cursor.execute(insert)

# READ Operation-
# query = f"SELECT * FROM Users"
# cursor.execute(query)

# # Fetch all the rows from the result set
# rows = cursor.fetchall()
# print(rows)

#UPDATE Operation
# Query = """update Users set city="Burhanpur" where id=1"""
# cursor.execute(Query)

#DELETE OPERATION
quer="""delete from users where id=3"""
cursor.execute(quer)

# Close the cursor and connection
# cursor.close()
connection.commit()