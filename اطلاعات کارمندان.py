import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pzthekabir",
  database = "mydatabase"
)
#mycursor.execute("CREATE TABLE customers (Name VARCHAR(255), Weight SMALLINT, Height SMALLINT)")
#sql = "INSERT INTO customers (Name, Weight, Height) VALUES (%s, %s, %s)"
#val = ("Arshia", 65, 185)
mycursor = mydb.cursor()
#mycursor.execute(sql, val)
#mydb.commit()
mycursor.execute("SELECT * FROM customers")
records = mycursor.fetchall()
rec_list = []
for record in records:
    rec_list.append(record)
sort_reclist = sorted(rec_list, key=lambda x: (x[2],-x[1]), reverse=True)
for name,weight,height in sort_reclist:
    print(name,height,weight)
#print(mycursor.rowcount, "record inserted.")

