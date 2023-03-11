import mysql.connector
class elo():
    def connect():
        return  mysql.connector.connect(host="localhost",password="1905",user="root", database="biblioteka")
    def ShowBooks():
        mydb = elo.connect()
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT * FROM books;")
        
        myresult = mycursor.fetchall()
        
        for x in myresult:
            print(x)
    def AddBook(title,author,genre):
        mydb = elo.connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO books(title,author,genre) VALUES (%s,%s,%s)"
        val = (title,author,genre)
        mycursor.execute(sql, val)
        mydb.commit()
