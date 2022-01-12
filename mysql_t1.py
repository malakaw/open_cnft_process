from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import httpc as hc

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'ddd'
 
mysql = MySQL(app)



def tom():
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO rank (name,volume,total_tx,total_assets,floor_price) VALUES(%s,%s,%s,%s,%s)''',
                   ("pavia",1,1,1,1))
        mysql.connection.commit()
        cursor.close()
        print ""


        

if __name__ == "__main__":
    tom()

