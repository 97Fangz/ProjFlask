import sys
import os

# Determine the project directory (one level up from the current script's location)
project_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(project_dir)
sys.path.append(project_dir)

from flask_post import app, BlogPost

# Set up the application context
app.app_context().push()

# Print a message before querying the database
print("Querying the database...")

# Query all blog posts
all_posts = BlogPost.query.all()

# Print a message after querying the database
print("Database query complete.")

# Print the titles of all blog posts
for post in all_posts:
    print(post.title)
