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
post_to_update = BlogPost.query.get(1)  # Replace 1 with the actual ID of the post you want to update

# Update the post's attributes
post_to_update.title = "Updated Title"
post_to_update.content = "Updated content"
post_to_update.author = "Updated Author"

# Commit the changes to the database
db.session.commit()

print("Post updated successfully")
