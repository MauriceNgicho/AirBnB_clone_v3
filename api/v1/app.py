#!/usr/bin/python3
"""
Flask web application for AirBnB API
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

