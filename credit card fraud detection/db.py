import sqlite3
# top=sqlite3.connect("credit_check")
# top.execute("""CREATE TABLE USERDATA(NAME TEXT,AGE INT,USERNAME TEXT PRIMARY KEY,PASSWORD TEXT)""")
# print("db created successfully")


top=sqlite3.connect("credituser_check")

# top.execute("""CREATE TABLE CREDIT(UID INT PRIMARY KEY,NAME TEXT,CNO TEXT,CVV INT,COUNTRY TEXT,CREDIT_LIMIT INT)""")
top.execute("""INSERT INTO CREDIT VALUES (01,'KIRAN','2222 4053 4324 8877',111,'INDIA',5000)""")
top.execute("""INSERT INTO CREDIT VALUES (02,'VIJAY','2222 9909 0525 7051',222,'INDIA',6000)""")
top.execute("""INSERT INTO CREDIT VALUES (03,'REENA','2223 0076 4872 6984',333,'INDIA',7000)""")
top.execute("""INSERT INTO CREDIT VALUES (04,'VEENA','2223 5771 2001 7656',444,'INDIA',8000)""")
top.execute("""INSERT INTO CREDIT VALUES (05,'SURYA','5105 1051 0510 5100',555,'INDIA',9000)""")
top.commit()
top.close() 

