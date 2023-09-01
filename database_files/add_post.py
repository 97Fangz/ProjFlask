import sys
import os

# Determine the project directory (one level up from the current script's location)
project_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(project_dir)
sys.path.append(project_dir)

from flask_post import app, BlogPost, db

# Set up the Flask application context
app.app_context().push()

# Create a new blog post
new_post = BlogPost(title="New Blog Post", content="This is the content of the new post", author="John Doe")

# Add the new post to the database
with app.app_context():
    db.session.add(new_post)
    db.session.commit()

print("New post added successfully")
