"""
API HTTP method practice for muscle memory.
"""


import requests

# Base URL for the API
base_url = "http://localhost:8000"

# New todo data
new_todo = {
    "title": "Learn Python requests library",
    "description": "Complete a course on Python API calls.",
    "done": False
}

# Send POST request
response = requests.post(f"{base_url}/todos", json=new_todo)

# Check if the request was successful
if response.status_code == 201:
    print("Request successful!")
    todo_item = response.json()
    id = todo_item["id"]
    get_response = requests.get(f"{base_url}/todos/{id}")  # get request
    todo_data = get_response.json()
    
    if get_response.status_code == 200:
        print("Request successful")
        print(f"New Todo: {todo_data}")
        
    else:
        print("Request error")
        print(f"Error code: {get_response.status_code}")
    # TODO: Retrieve the id from the stored response json
    
    # TODO: Use the retrieved id to perform a GET request with it
    
    # TODO: Check if the GET request was successful and print the new todo item
        # TODO: Handle potential errors from the GET request
else:
    # Handle potential errors from the POST request
    print("Failed to add a new todo")
    print(f"Status Code: {response.status_code}")
    print(f"Error Details: {response.json()}")