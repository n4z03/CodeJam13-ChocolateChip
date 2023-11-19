from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from src.NotificationQueue import NotificationQueue
from src.Notification import DateIncrement
from datetime import datetime
import json
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # SQLite database file
db = SQLAlchemy(app)

app.secret_key = 'luisisaacnazrup' #Session key
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Initialize column in database for id
    name = db.Column(db.String(100)) # Initialize column in database for name
    password = db.Column(db.String(100)) # Initialize column in databasefor password
    email = db.Column(db.String(100))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100))
    name = db.Column(db.String(100))
    type = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    email = db.Column(db.String(100))
    social_media = db.Column(db.String(100))
    date = db.Column(db.String(100))
    c_day = db.Column(db.String(100))
    c_month = db.Column(db.String(100))
    c_year = db.Column(db.String(100))
    f_day = db.Column(db.String(100))
    f_week = db.Column(db.String(100))
    f_month = db.Column(db.String(100))
    f_year = db.Column(db.String(100))
    def __init__(self, user_email = None, name = None, type = None, phone_number = None, email = None, social_media = None, c_day = None, c_month = None, c_year = None, f_day = None, f_week = None, f_month = None, f_year = None):
        self.user_email = user_email
        self.name = name
        self.type = type
        self.phone_number = phone_number
        self.email = email
        self.social_media = social_media
        self.c_day = c_day
        self.c_month = c_month
        self.c_year = c_year
        self.f_day = f_day
        self.f_week = f_week
        self.f_month = f_month
        self.f_year = f_year

    def get_date(self):
        return datetime(int(self.c_year), int(self.c_month), int(self.c_day))

    def __lt__(self, other):
        return self.get_date() < other.get_date()

with app.app_context():
    notification_queue = NotificationQueue()
    # Home route
    @app.route('/')
    def index():
        # Check if the user is logged in
        logged_in = session.get('logged_in', False)
        if logged_in:
            contacts = Contact.query.all()
            return render_template('chip-viewer.html', contacts = contacts)
        else:
            return render_template('index.html')

    # Process to handle signups, and storing user into the database
    @app.route('/process', methods=['POST'])
    def process():
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        # Check if the user is in the database already
        user = User.query.filter_by(name=name).first()
        if not user:
            new_user = User(name=name, password=password, email=email)
            db.session.add(new_user)
            db.session.commit()

            session['name'] = name
            session['logged_in'] = True
            session['email'] = email
            # Return on signup (could change to an html file)
            contacts = Contact.query.all()
            return render_template("chip-viewer.html", username = name, contacts = contacts)
        else:
            error = "Username already exists please try again."
            return render_template("signup.html", error = error)
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
            email = request.form['email']
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
        if not session.get('logged_in'):
            contacts = Contact.query.all()
            for contact in contacts:
                if contact:
                    notification = Notification(contact)
                    if not notification_queue.exists(notification):
                        notification_queue.add_notification(notification)

            return render_template("chip-viewer.html", contacts = contacts)
        
        else:
            contacts = Contact.query.all()
            return render_template("chip-viewer.html", contacts = contacts)
  
    @app.route('/addChip', methods=['POST'])
    def add_chip():
        name = None
        type = None
        email = None
        phone = None
        social = None
        
        data = request.json.get('data')
        print (data)
        for key in data:
            if key == "name":
                name = data[key]
            elif key == "type":
                type = data[key]
            elif key == "email":
                email = data[key]
            elif key == "phone number":
                phone = data[key]
            elif key == "social media":
                social = data[key]
        
        # Process the keys and values as needed (e.g., store in database)
        # Example: Printing keys and values
        contact = Contact(session['name'], name, type, phone, email, social)
        db.session.add(contact)
        db.session.commit()
        
        # Redirect to view contacts
        return redirect('chipviewer')
    
    @app.route('/createcontact')
    def createchip():
        return render_template('createcontact.html')
    
    if __name__ == '__main__':
        db.create_all()  # Create tables based on defined models
        app.run(debug=True)
