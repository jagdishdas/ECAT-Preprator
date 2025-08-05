# Main entry point for the ECAT Prep Platform
# This file imports the Flask app from the server directory

import sys
import os

# Add the server directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'server'))

from server.main import app  # Import from server/main.py

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)