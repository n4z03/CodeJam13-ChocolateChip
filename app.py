from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database file
db = SQLAlchemy(app)

app.secret_key = 'luisisaacnazrup' #Session key
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Initialize column in database for id
    name = db.Column(db.String(100)) # Initialize column in database for name
    password = db.Column(db.String(100)) # Initialize column in databasefor password

with app.app_context():
    # Home route
    @app.route('/')
    def index():
        # Check if the user is logged in
        logged_in = session.get('logged_in', False)
        if logged_in:
            username = session.get('name')
            return render_template('chip-viewer.html', username = username)
        else:
            return render_template('index.html')

    # Process to handle signups, and storing user into the database
    @app.route('/process', methods=['POST'])
    def process():
        name = request.form['name']
        password = request.form['password']

        # Add user to database
        new_user = User(name=name, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Return on signup (could change to an html file)
        return "Data stored successfully!"

    # Display the users in database
    @app.route('/users')
    def get_users():
        users = User.query.all()
        return render_template('users.html', users=users)

     # Route handles login
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            # Check if the user is in the database
            user = User.query.filter_by(name=username, password=password).first()
            if user:
                # Redirect to a success page or perform an action upon successful login
                session['name'] = username
                session['logged_in'] = True
                return render_template('chip-viewer.html', username = session['name'])
            else:
                # Output an error message
                error = "Invalid username or password. Please try again."
                return render_template('login.html', error=error)
            
        return render_template('login.html')
    # Remove the user from the session
    @app.route('/logout')
    def logout():
        session.pop('logged_in', None)
        session.pop('name', None)
        return "Logged out, session ended."
    
    @app.route('/signup')
    def signup():
        return render_template('signup.html')
    
    @app.route('/chipviewer')
    def chipviewer():
        
        return render_template("chip-viewer.html")
    
    if __name__ == '__main__':
        db.create_all()  # Create tables based on defined models
        app.run(debug=True)
