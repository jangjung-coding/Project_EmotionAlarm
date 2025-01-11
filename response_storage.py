# response_storage.py

import json

# File to store data
DATA_FILE = "responses.json"

def save_response(question, response):
    # Load existing data
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Add new response
    data.append({"question": question, "response": response})

    # Save updated data
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def load_responses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
