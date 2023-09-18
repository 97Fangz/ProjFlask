import sys
import os

# Determine the project directory (one level up from the current script's location)
project_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(project_dir)
sys.path.append(project_dir)

from flask_post import app, db

# Creates an application context
with app.app_context():
    # Creates the database tables
    db.create_all()
    
print("Database tables created successfully")
