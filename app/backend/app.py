from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import pooling
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
CORS(app)

dbconfig = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "database": os.getenv("DB_NAME", "auth_db")
}
pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **dbconfig)

# Create users table
conn = pool.get_connection()
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
)
""")
conn.commit()
cursor.close()
conn.close()

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    hashed = generate_password_hash(password)
    conn = pool.get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (email,password) VALUES (%s,%s)", (email, hashed))
        conn.commit()
        return jsonify({"message":"Sign up successful"})
    except mysql.connector.IntegrityError:
        return jsonify({"message":"User exists"}), 400
    finally:
        cursor.close()
        conn.close()

@app.route("/signin", methods=["POST"])
def signin():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    conn = pool.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user and check_password_hash(user[0], password):
        return jsonify({"message":"Sign in successful"})
    return jsonify({"message":"Invalid credentials"}), 401

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    cursor.close()
    conn.close()
    if user and check_password_hash(user[0], password):
        return jsonify({"message":"Sign in successful"})
    return jsonify({"message":"Invalid credentials"}), 401

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


