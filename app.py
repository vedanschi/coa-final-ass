from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
def get_db_connection():
    connection = mysql.connector.connect(
        host='mysql-container',  # Hostname of the MySQL container
        user='root',
        password='root',
        database='mydb'
    )
    return connection

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

