from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import httpc as hc

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'ddd'
 
mysql = MySQL(app)



def exec_sql(sql_):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute(sql_)
        mysql.connection.commit()
        cursor.close()



#        cursor.execute(''' INSERT INTO rank (name,volume,total_tx,total_assets,floor_price) VALUES(%s,%s,%s,%s,%s)''',
#                   ("pavia",1,1,1,1))

        

if __name__ == "__main__":
    exec_sql("")

