#!c:\Python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

Form=cgi.FieldStorage()

FFullName=Form.getvalue('name')
FEmail=Form.getvalue('email')
FTypeYourMessage=Form.getvalue('message')

print("<h3>Thank You for Registering!!!</h3>")
print("<h1>",FFullName,FEmail,FTypeYourMessage,"</h1>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="warriors"
)

mycursor=mydb.cursor();

sql="INSERT INTO enquiry(FullName,Email,Message) VALUES(%s,%s,%s)";
val=(FFullName,FEmail,FTypeYourMessage)

mycursor.execute(sql,val)
mydb.commit()

print("</body>")
print("</html>")