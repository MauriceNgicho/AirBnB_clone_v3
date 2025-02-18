#!/usr/bin/python3
"""
Defines API routes for status check.
"""
from Flask import flask, jsonify
from api.v1.views import app_views

@app_views.route("/states", methods=['GET'], strict_slashes=False)
def status():
    """Returns API status"""
    return jsonify({"status": "OK"})
