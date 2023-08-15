from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required
from flask import request, jsonify, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db) 


@app.route('/')
def hello_world():
    return 'Hello, World!'

#...................................................................................database

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)


#......................................................................................login

login_manager = LoginManager(app)
# ... other app configurations ...

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['POST'])
def register():
    # Implement user registration logic here
    pass

@app.route('/login', methods=['POST'])
def login():
    # Implement user login logic here
    pass

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    # Return a response indicating successful logout
    pass

#.......................................................................................event
@app.route('/api/events', methods=['GET'])
def get_events():
    # Implement logic to retrieve a list of events
    # Retrieve a list of events from the database
    events = Event.query.all()

    # Create a list to hold event data
    event_list = []

    # Iterate through the events and extract relevant information
    for event in events:
        event_data = {
            "id": event.id,
            "title": event.title,
            "date": event.date,  # Convert date to string
            "time": event.time,  # Convert time to string
            "location": event.location,
            "description": event.description,
            "available_seats": event.available_seats
        }
        event_list.append(event_data)

    return jsonify(event_list)

@app.route('/api/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    # Implement logic to retrieve details of a specific event
    pass

@app.route('/api/events', methods=['POST'])
#@login_required
def create_event():
    # Get data from the JSON request
    event_data = request.json
    
    # Extract event details from the data
    title = event_data.get('title')
    date = event_data.get('date')
    time = event_data.get('time')
    location = event_data.get('location')
    description = event_data.get('description')
    available_seats = event_data.get('available_seats')
    
    # Create a new event
    new_event = Event(
        title=title,
        date=date,
        time=time,
        location=location,
        description=description,
        available_seats=available_seats
    )
    
    # Add the event to the database
    db.session.add(new_event)
    db.session.commit()
    
    return jsonify({"message": "Event created successfully"})

    # Implement logic to create a new event
    



@app.route('/api/events/<int:event_id>', methods=['DELETE'])
#@login_required
def delete_event(event_id):
    # Find the booking by ID
    event = Event.query.get(event_id)

    if not event:
        return jsonify({"message": "event not found"}), 404

    # Check if the logged-in user is the owner of the booking
   # if booking.user_id != current_user.id:
    #    return jsonify({"message": "You do not have permission to delete this booking"}), 403

    # Delete the booking from the database
    db.session.delete(event)
    db.session.commit()

    return jsonify({"message": "event deleted successfully"})

# ..................................................................................................booking




@app.route('/api/bookings', methods=['POST'])
@login_required
def create_booking():
    # Implement logic to create a new booking
    pass

@app.route('/api/bookings/<int:booking_id>', methods=['GET'])
@login_required
def get_booking(booking_id):
    # Implement logic to retrieve details of a specific booking
    pass

if __name__ == '__main__':
    app.run(debug=True)

