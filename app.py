from flask import Flask, request , render_template,redirect
from flask_mysqldb import MySQL 
from biblioteka import elo

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1905'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'biblioteka'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def path():
    return redirect("/mainSite")

@app.route('/mainSite')
def index():
    return render_template("mainSite.html")

@app.route('/mainSite', methods=['POST'])
def main():
    if request.form['do']=="show":
        return redirect("/mainSite/DB")
    elif request.form['do']=="add":
        return redirect("/mainSite/AddBook")

@app.route('/mainSite/DB')
def show():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM books;")
        results = cur.fetchall()
        print(results)
        b="<center><table border='1'width='100%'>"
        for i in range(len(results)):
            a= "<tr><td>"+str(results[i]["id"])+"<td>"+str(results[i]["title"])+"<td>"+str(results[i]["author"])+"<td>"+str(results[i]["genre"])
            b=b+a
        return b

@app.route('/mainSite/AddBook')
def cos():
     return render_template("index.html")

@app.route('/mainSite/AddBook', methods=['POST'])
def addBook():
        title = request.form['title']
        author = request.form['author']
        genre = request.form["genre"]
        elo.AddBook(title,author,genre)
        return redirect("/mainSite/AddBook")