from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database file
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))

with app.app_context():
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/process', methods=['POST'])
    def process():
        name = request.form['name']
        password = request.form['password']

        new_user = User(name=name, password=password)
        db.session.add(new_user)
        db.session.commit()

        return "Data stored successfully!"

    @app.route('/users')
    def get_users():
        users = User.query.all()
        return render_template('users.html', users=users)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['name']
            password = request.form['password']
            
            user = User.query.filter_by(name=username, password=password).first()
            if user:
                # Redirect to a success page or perform an action upon successful login
                return redirect(url_for('success'))
            else:
                # Output an error message
                error = "Invalid username or password. Please try again."
                return render_template('login.html', error=error)
        
        return render_template('login.html')
    
    @app.route('/success')
    def success():
        return "Login successful! Welcome to the success page."

    @app.route('/signup')
    def signup():
        return render_template('signup.html')
    if __name__ == '__main__':
        db.create_all()  # Create tables based on defined models
        app.run(debug=True)
