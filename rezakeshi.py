import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="**",
)
mycursor = mydb.cursor()

sql = "CREATE DATABASE stationery_shop"
mycursor.execute(sql)

mydb = mysql.connemctor.connect(
 host="localhost",
 user="root",
 passwd="**",
   database="stationery_shop"
)
mycursor = mydb.cursor()

sql = """
 CREATE TABLE products(
 id INT auto_incerement,
 name VARCHAR(250),
 price INT,
 quantity INT,
 category_id INT,
 PRIMARY KEY(id),
 FOREIGN KEY(category_id) REFERENCES categories(id)
 );
 """
mycursor.execute(sql)

sql = """
 CREATE TABLE categories(
 id INT auto_incerement,
 name VARCHAR(250),
 PRIMARY KEY(id)
 );
 """
mycursor.execute(sql)

sql = "INSERT INTO categories(id,name)"
sql = "VALUES (1,'Office supplies')"
mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO categories(id,name)"
sql = "VALUES (2,'Educational supplies')"
mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO categories(id,name)"
sql = "VALUES (3,'Art supplies')"
mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO products(id,name,category_id,price,quantity)"  
sql = " VALUES (1,'Ballpoint pen',1,1000,100)"
mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO products(id,name,category_id,price,quantity)"  
sql = " VALUES (2,'Pencil',1,500,200)"
mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO products(id,name,category_id,price,quantity)"  
sql = " VALUES (3,'Eraser',1,200,300)"
mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO products(id,name,category_id,price,quantity)"  
sql = " VALUES (4,'Notebook',2,1500,500)"
mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO products(id,name,category_id,price,quantity)"  
sql = " VALUES (5,'Book',2,5000,1000)"
mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO products(id,name,category_id,price,quantity)"  
sql = " VALUES (6,'Crayons',3,3000,200)"
mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO products(id,name,category_id,price,quantity)"  
sql = " VALUES (7,'Paints',3,5000,1000)"
mycursor.execute(sql)
mydb.commit()

sql = "SELECT * FROM products"
mycursor.execute(sql)
mycursor.fetchall()
sql = "UPDATE products SET price = 0.3 * price + price"
mycursor.execute(sql)

sql = "SELECT * FROM products WHERE name = Ballpoint pen"
mycursor.execute(sql)
mycursor.fetchall()

sql = "SELECT name FROM products"
mycursor.execute(sql)
mycursor.fetchall()

sql = "SELECT name FROM categories"
mycursor.execute(sql)
mycursor.fetchall()