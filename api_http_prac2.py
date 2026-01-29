import requests

# Base URL for the API
base_url = "http://localhost:8000"

# Helper function named to handle unexpected status codes


def handle_error(response):
    """Print error details from the response."""
    print("Error occurred")
    print(f"Status Code: {response.status_code}")
    print(f"Error Details: {response.json()}")

# TODO: Define a function named `put_todo` to handle PUT requests.
# - The function should take `todo_id` and `data` as parameters.
# - Construct the PUT request URL using `base_url` and `todo_id`, send the request, and check the response status.
# - Print a success message and the response JSON if the status code is 200, otherwise call `handle_error`.


def put_todo(todo_id, data):
    response_put = requests.put(f"{base_url}/todos/{todo_id}", json=data)
    if response_put.status_code == 200:
        print("Request successful")
        print(f"Data: {response_put.json()}")
    else:
        handle_error(response_put)

# TODO: Define a function named `patch_todo` to handle PATCH requests.
# - The function should take `todo_id` and `data` as parameters.
# - Construct the PATCH request URL using `base_url` and `todo_id`, send the request, and check the response status.
# - Print a success message and the response JSON if the status code is 200, otherwise call `handle_error`.


def patch_todo(todo_id, data):
    response_patch = requests.patch(f"{base_url}/todos/{todo_id}", json=data)
    if response_patch.status_code == 200:
        print("Request successful")
        print(f"Data: {response_patch.json()}")
    else:
        handle_error(response_patch)
        

# TODO: Define a function named `delete_todo` to handle DELETE requests.
# - The function should take `todo_id` as a parameter.
# - Construct the DELETE request URL using `base_url` and `todo_id`, send the request, and check the response status.
# - Print a success message if the status code is 204, otherwise call `handle_error`.


def delete_todo(todo_id):
    response_delete = requests.delete(f"{base_url}/todos/{todo_id}")
    if response_delete.status_code == 204:
        print("Request successful")
    else:
        handle_error(response_delete)

# Update a complete todo item using PUT


put_todo(todo_id=1, data={
    "title": "Buy groceries and snacks",
    "description": "Milk, eggs, bread, coffee, and chips.",
    "done": True
})


# Partially update a todo item using PATCH
patch_todo(todo_id=2, data={"description": "Updated description"})

# Delete a todo item using DELETE
delete_todo(todo_id=3)