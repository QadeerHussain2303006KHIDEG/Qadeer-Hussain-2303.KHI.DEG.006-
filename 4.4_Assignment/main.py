import json
import logging
import os
import sys

from flask import Flask, render_template, request

app = Flask(__name__)

# Check if DEBUG environment variable is set to "1"
debug=os.environ.get("DEBUG")=="1"

# If DEBUG is enabled, set logging level to DEBUG and set format
if debug:
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
# If DEBUG is disabled, set logging level to INFO and set format
else:
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')


# Set path to todo list file
TODO_FILE_PATH = "/app/data/todo.json"


# If todo list file exists, load it and assign it to TODO_ITEMS
if os.path.exists(TODO_FILE_PATH):
    with open(TODO_FILE_PATH) as f:
        TODO_ITEMS = json.load(f)
# If todo list file does not exist, set TODO_ITEMS to an empty list
else:
    TODO_ITEMS = []


# Define a function to periodically save the todo list to the file
def periodically_save_todo_items():
    with open(TODO_FILE_PATH, "w") as f:
        json.dump(TODO_ITEMS, f)

# Define the main route for the app
@app.route("/", methods=["GET", "POST"])
def main():
    # If the request method is POST, a new todo item is being added
    if request.method == "POST":
        content = request.form["content"]
        TODO_ITEMS.append(content)
        # Periodically save the updated todo list
        periodically_save_todo_items()

    # Render the index template with the current todo list
    return render_template("index.html", todo_items=TODO_ITEMS)

# Start the Flask app if this file is being run directly
if __name__ == "__main__":
    app.run(host="0.0.0.0")
