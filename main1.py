from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3
import psycopg2



app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="database_perpustakaan_db",
        user="postgres_db",
        password="1_db",
        host="localhost"
    )
    return conn

@app.route('/da')
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, nama, umur FROM users')
    daftar_users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('daftar.html', users=daftar_users)

conn = sqlite3.connect('database.db')
c = conn.cursor()



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1@localhost/belajar'


@app.route("/awal")
def home():
    web_title = "awal Page"
    return render_template('INDEX.html')


@app.route("/penulis")
def penulis():
    web_title = "Penulis Page"
    return render_template
('penulis/penulis.html')

@app.route("/penerbit")
def penerbit():
    web_title = "Penerbit Page"
    return render_template('penerbit/penerbit.html')

@app.route("/dashboard")
def dashboard():
    web_title = "Dashboard Page"
    return render_template('dashboard.html')

@app.route('/submit', methods=['post'])
def submit():
    judul_buku= request.form['judul_buku']
    penulis= request.form['penulis']
    penerbit= request.form['penerbit']

@app.route("/daftar")
def daftar_buku():
    web_title = "Daftar Buku"
    conn = sqlite3.connect('database.db')
    c.execute("SELECT * FROM buku")
    
    judul_buku = c.fetchall()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=8080)