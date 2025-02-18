#!/usr/bin/python3
"""
Initialize the Blueprint for API routes.
"""

from flask import Blueprint

# Create a Flask Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import all views
from api.v1.views.index import *
