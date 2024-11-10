from flask import Flask, render_template, request, url_for

app = Flask(__name__)
#homepage route
@app.route("/")
#connecting to database
def index():
    return "Welcome to the Flashcard App!"



if __name__ == "__main__":
    app.run(debug=True)