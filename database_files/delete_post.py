import sys
import os

# Determine the project directory (one level up from the current script's location)
project_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(project_dir)
sys.path.append(project_dir)

from flask_post import app, BlogPost, db

# Set up the Flask application context
app.app_context().push()

# Query an existing blog post by its ID
post_to_delete = BlogPost.query.get(1)  # Replace 1 with the actual ID of the post you want to delete

# Delete the post from the database
db.session.delete(post_to_delete)
db.session.commit()

print("Post deleted successfully")
