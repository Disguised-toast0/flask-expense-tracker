from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
    return render_template("index.html")


@app.get('/login')
def login():
    return render_template("login.html")
    
@app.get('/expense')
def expense():
    return render_template("expense.html")


if __name__ == '__main__':
    app.run(debug=True)