from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todos.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# class Todo(db.Model):
#         sno = db.column


@app.route('/')
def dashboard():
    return render_template('index.html')


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, port=8000)
