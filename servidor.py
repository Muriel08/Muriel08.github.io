from flask import Flask, render_template, request, redirect, url_for, flash, session 
from flask_mysqldb import MySQL 


app = Flask(__name__)

# Conneted MySQL
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = ''

mysql = MySQL(app)

#settings
app.secret_key="tamara"


@app.route("/")
def main():
    return render_template("index.html")


if __name__== "__main__":
    app.run(port = 3002, debug=True)


