# Dictionary to store user data
user_database = {}

# Function to create a new user
def create_user(id, name, email, phone_number, password):
    user_info = {
        "id": id,
        "name": name,
        "email": email,
        "phone_number": phone_number,
        "password": password
    }
    user_database[id] = user_info
    return user_info

# Function to retrieve user information by id
def get_user(id):
    if id in user_database:
        return user_database[id]
    else:
        return None

# Function to get user input
def get_user_input():
    id = int(input("Enter User ID: "))
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone_number = input("Enter Phone Number: ")
    password = input("Enter Password: ")
    return id, name, email, phone_number, password

# Example usage:
if __name__ == "__main__":
    # Prompt the user to create a new user
    id, name, email, phone_number, password = get_user_input()
    user1 = create_user(id, name, email, phone_number, password)
    print("User created with ID:", id)

    # Prompt the user to retrieve user information by id
    user_id_to_retrieve = int(input("Enter User ID to Retrieve: "))
    retrieved_user = get_user(user_id_to_retrieve)

    if retrieved_user:
        print("User ID:", retrieved_user["id"])
        print("Name:", retrieved_user["name"])
        print("Email:", retrieved_user["email"])
        print("Phone Number:", retrieved_user["phone_number"])
        # Do not print the password for security reasons
    else:
        print("User not found.")