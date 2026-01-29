import requests

# Base URL for the API
base_url = "http://localhost:8000"

# Helper function named to handle unexpected status codes
def handle_error(response):
    """Print error details from the response."""
    print("Error occurred")
    print(f"Status Code: {response.status_code}")
    print(f"Error Details: {response.json()}")

# Handle GET requests to retrieve all todo items
def get_all_todos():
    response_get_all = requests.get(f"{base_url}/todos")
    if response_get_all.status_code == 200:
        todos = response_get_all.json()
        print("\nAll todos retrieved successfully!")
        for todo in todos:
            print(f"ID: {todo['id']}, Title: '{todo['title']}', Description: '{todo['description']}', Done: {todo['done']}")
    else:
        handle_error(response_get_all)

# Handle POST requests to create a new todo item
def post_todo(data):
    response_post = requests.post(f"{base_url}/todos", json=data)
    if response_post.status_code == 201:
        print("Todo created successfully!")
        print(response_post.json())
    else:
        handle_error(response_post)

# Handle PUT requests to update a full todo item
def put_todo(todo_id, data):
    response_put = requests.put(f"{base_url}/todos/{todo_id}", json=data)
    if response_put.status_code == 200:
        print("Todo updated successfully with PUT!")
        print(response_put.json())
    else:
        handle_error(response_put)

# Handle PATCH requests to update part of a todo item
def patch_todo(todo_id, data):
    response_patch = requests.patch(f"{base_url}/todos/{todo_id}", json=data)
    if response_patch.status_code == 200:
        print("Todo updated successfully with PATCH!")
        print(response_patch.json())
    else:
        handle_error(response_patch)

# Handle DELETE requests to remove a todo item
def delete_todo(todo_id):
    response_delete = requests.delete(f"{base_url}/todos/{todo_id}")
    if response_delete.status_code == 204:
        print("Todo deleted successfully!")
    else:
        handle_error(response_delete)

# Call appropriate functions based on the provided scenarios
# Use:
# - patch_todo() for partial updates
# - put_todo() for full updates
# - delete_todo() for removing items
# - post_todo() for adding new items
# - Verify the final state with get_all_todos()


# Update ID 1 (partial update)
patch_todo(1, {
    "title": "Buy groceries and snacks",
    "description": "Milk, eggs, bread, coffee, and chips"
})

# Delete ID 2
delete_todo(2)

# Update ID 3 (title change + mark as done)
put_todo(3, {
    "title": "Complete project report",
    "description": "Summarize Q4 performance metrics",
    "done": True
})

# Delete ID 4
delete_todo(4)

# Create ID 5
post_todo({
    "title": "Read new book",
    "description": "Start reading 'Atomic Habits'",
    "done": False
})

# Create ID 6
post_todo({
    "title": "Attend yoga class",
    "description": "Morning session",
    "done": False
})

# Verify final state
get_all_todos()
