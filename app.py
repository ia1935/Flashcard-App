from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('flashcards.db')
    conn.row_factory = sqlite3.Row
    return conn

# Homepage route
@app.route("/")
def index():
    conn = get_db_connection()
    flashcards = conn.execute('SELECT * FROM flashcards').fetchall()
    conn.close()
    return render_template('index.html', flashcards=flashcards)

# Route for adding a new flashcard
@app.route('/add', methods=['GET', 'POST'])
def add_flashcard():
    if request.method == 'POST':  # If the form is submitted
        question = request.form['question']
        answer = request.form['answer']
        
        # Insert the new flashcard into the database
        conn = get_db_connection()
        conn.execute('INSERT INTO flashcards (question, answer) VALUES (?, ?)', (question, answer))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))  # Redirect to the homepage

    return render_template('add_flashcard.html')


@app.route('/delete/<int:card_id>')
def delete_flashcard(card_id):
    conn = get_db_connection()
    conn.execute('delete from flashcards where id=?',(card_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
