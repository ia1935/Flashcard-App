from flask import Flask, render_template, request, url_for
import sqlite3

app = Flask(__name__)
#homepage route
@app.route("/")
#connecting to database


def get_db_connection():
    conn = sqlite3.connect('flashcards.db')
    conn.row_factory = sqlite3.Row
    return conn

def index():
    conn = get_db_connection()
    flashcards = conn.execute('select * from flashcards').fetchall()
    conn.close()
    #homepage template
    return render_template('index.html',flashcards=flashcards)



if __name__ == "__main__":
    app.run(debug=True)