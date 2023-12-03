# Django Custom Authentication App

This Django app provides a custom authentication system with APIs for user registration, login, user details retrieval, user details update, user account deletion, and user logout.

## API Documentation

### 1. User Registration and Login

#### Endpoint: /api/users/register
- Method: POST
- Functionality: Allows a new user to create an account.
- Input: Name, username, bio, age, password.
- Output: Confirmation of account creation, user details.

#### Endpoint: /api/users/login
- Method: POST
- Functionality: Authenticates an existing user.
- Input: Username and password.
- Output: Authentication token, user details.

### 2. Get User Details

#### Endpoint: /api/users/details
- Method: GET
- Functionality: Retrieves the details of the logged-in user.
- Input: User's authentication token.
- Output: User's details (name, username, bio, age).

### 3. Update User Details

#### Endpoint: /api/users/update
- Method: PUT
- Functionality: Allows a user to update their profile details.
- Input: User's authentication token, updated details (name, username, bio, age).
- Output: Confirmation of update, updated user details.

### 4. Delete User Account

#### Endpoint: /api/users/delete
- Method: DELETE
- Functionality: Allows a user to permanently delete their account.
- Input: User's authentication token.
- Output: Confirmation of account deletion.

### 5. User Logout

#### Endpoint: /api/users/logout
- Method: POST
- Functionality: Logs out the user, invalidating their current authentication token.
- Input: User's authentication token.
- Output: Confirmation of logout.

## cURL Examples

```bash
# User Registration
curl --location 'http://127.0.0.1:8000/api/users/register' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Christopher Williams",
    "username": "chris1234",
    "age": 32,
    "bio": "A musician exploring the world of jazz.",
    "password": "1234"
}'

# User Login
curl --location 'http://127.0.0.1:8000/api/users/login' \
--header 'Content-Type: application/json' \
--data '{
  "username": "chris1234",
  "password": "1234"
}'

# Get User Details
curl --location 'http://127.0.0.1:8000/api/users/details' \
--header 'Authorization: <USER_AUTH_TOKEN>' \
--data ''

# Update User Details
curl --location --request PUT 'http://127.0.0.1:8000/api/users/update' \
--header 'Authorization: <USER_AUTH_TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Christopher Williams 2",
    "username": "chris1234",
    "age": 32,
    "bio": "A musician exploring the world of jazz.",
    "password": "1234"
}'

# Delete User Account
curl --location --request DELETE 'http://127.0.0.1:8000/api/users/delete' \
--header 'Authorization: <USER_AUTH_TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
    "password":"mikebrown123"
}'

# User Logout
curl --location --request POST 'http://127.0.0.1:8000/api/users/logout' \
--header 'Authorization: <USER_AUTH_TOKEN>'
```

## Installation

1. Clone the project from GitHub:
   ```bash
   git clone https://github.com/abhishek-rajput119/authentication.git

2. Go to base directory:
    ```bash
   cd authentication

3. Create a virtual environment:
   ```bash
   python -m venv venv_name
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv_name\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source venv_name/bin/activate
     ```

5. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

6. Migrate the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Accessing the Application

To interact with the API, you can use tools like cURL,Postman or your web browser.

1. Open your web browser.

2. Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

3. Explore the provided API endpoints for user registration, login, details retrieval, update, deletion, and logout.


