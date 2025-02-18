#!/usr/bin/python3
"""
Flask Web API for the AirBnB Clone project.

This script initializes and runs a Flask web application that serves 
as the API backend for the AirBnB Clone project.

Key functionalities:
- Creates a Flask app instance.
- Registers the `app_views` Blueprint, which contains API routes.
- Closes the database storage session after each request.
- Configures the server to run on a specified host and port.

Environment Variables:
- HBNB_API_HOST: Defines the host IP (default: "0.0.0.0").
- HBNB_API_PORT: Defines the port number (default: 5000).

Dependencies:
- Flask
- models.storage (for database interaction)
- api.v1.views (contains API routes)
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

# Create Flask app
app = Flask(__name__)

# Register Blueprint
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_storage(exception):
    """Close storage session"""
    storage.close()

if __name__ == "__main__":
    # Set host and port from environment variables or use default values
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))

    # Run Flask server with threading enabled
    app.run(host=host, port=port, threaded=True)

