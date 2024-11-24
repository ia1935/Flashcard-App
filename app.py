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
    #sorting by group (categories)
    categories ={}
    for card in flashcards:
        if card['category'] not in categories:
            categories[card['category']] = []
        categories[card['category']].append(card)


    return render_template('index.html', categories=categories)

# Route for adding a new flashcard
@app.route('/add', methods=['GET', 'POST'])
def add_flashcard():
    if request.method == 'POST':  # If the form is submitted
        question = request.form['question']
        answer = request.form['answer']
        category = request.form['category']
        
        # Insert the new flashcard into the database
        conn = get_db_connection()
        conn.execute('INSERT INTO flashcards (question, answer, category) VALUES (?, ?, ?)', 
                     (question, answer, category))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))  # Redirect to the homepage

    return render_template('add_flashcard.html')


#route to edit flashcard
@app.route('/edit/<int:card_id>',methods=['GET','POST'])
def edit_flashcard(card_id):

    #connect to db
    conn = get_db_connection()

    #get the data matching the card_id
    flashcard = conn.execute('select * from flashcards where id=?',(card_id,)).fetchone()

    #no flashcard found handling
    if flashcard is None:
        return "Flashcard not found", 404
    
    #store edit info from dropdown
    if request.method == 'POST':
        updated_question = request.form['question']
        updated_answer = request.form['answer']

        #execute command to enter new values question, answer in the id location
        conn.execute('update flashcards set question = ?, answer = ? where id = ?',
                     (updated_question, updated_answer, card_id))  
        conn.commit()
        conn.close()
        return redirect(url_for('index')) #return to homepage after updating

    conn.close()
    return render_template('edit_flashcard.html', flashcard=flashcard)


@app.route('/delete/<int:card_id>')
def delete_flashcard(card_id):
    conn = get_db_connection()
    conn.execute('delete from flashcards where id=?',(card_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

@app.route('/delete_category/<category>', methods=['POST'])
def delete_category(category):
    conn = get_db_connection()
    conn.execute('delete from flashcards where category =?',(category,))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
