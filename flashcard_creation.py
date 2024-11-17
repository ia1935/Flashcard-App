# temporary file which will create our flashcard database

import sqlite3
#creating database
conn = sqlite3.connect('flashcards.db')

#cursor object to interact with db
c = conn.cursor()

#creating table:
c.execute('''
          create table flashcards(id integer primary key autoincrement, 
          question text not null,
          answer text not null, category text default 'Miscellaneous')
          
          
          ''')

conn.commit()
conn.close()
