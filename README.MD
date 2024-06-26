# FastAPI Web Application

This is a web application built with FastAPI, following the MVC design pattern. The application interfaces with a MySQL database using SQLAlchemy for ORM, and includes authentication, post creation, retrieval, and deletion functionalities.

## Features

- User Signup and Login with token-based authentication
- Create, retrieve, and delete posts
- In-memory caching for retrieved posts
- Dependency injection for database session and token verification
- Field validation using Pydantic models

## Endpoints

### User Endpoints

- **Signup**
  - **URL:** `/signup`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "email": "user@example.com",
      "password": "password123"
    }
    ```
  - **Response:**
    ```json
    {
      "access_token": "token_string",
      "token_type": "bearer"
    }
    ```

- **Login**
  - **URL:** `/login`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "email": "user@example.com",
      "password": "password123"
    }
    ```
  - **Response:**
    ```json
    {
      "access_token": "token_string",
      "token_type": "bearer"
    }
    ```

### Post Endpoints

- **Add Post**
  - **URL:** `/posts`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "text": "This is a new post"
    }
    ```
  - **Headers:**
    ```
    Authorization: Bearer token_string
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "text": "This is a new post",
      "user_id": 1
    }
    ```

- **Get Posts**
  - **URL:** `/posts`
  - **Method:** `GET`
  - **Headers:**
    ```
    Authorization: Bearer token_string
    ```
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "text": "This is a new post",
        "user_id": 1
      },
      ...
    ]
    ```

- **Delete Post**
  - **URL:** `/posts/{post_id}`
  - **Method:** `DELETE`
  - **Headers:**
    ```
    Authorization: Bearer token_string
    ```
  - **Response:**
    ```json
    {
      "message": "Post deleted successfully"
    }
    ```

## Setup and Installation

### Prerequisites

- Python 3.7+
- MySQL database

### Installation

1. **Clone the Repository**
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2. **Create and Activate a Virtual Environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up the Database**
    - Create a MySQL database.
    - Update the `SQLALCHEMY_DATABASE_URL` in `app/database.py` with your database credentials.

5. **Run Database Migrations**
    - Use a tool like Alembic to manage your database migrations.

6. **Run the Application**
    ```bash
    uvicorn app.main:app --reload
    ```

### Testing the Endpoints

You can test the endpoints using tools like Postman or CURL.

## Project Structure

my_app/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── models/
│ │ ├── init.py
│ │ └── user.py
│ │ └── post.py
│ ├── schemas/
│ │ ├── init.py
│ │ └── user.py
│ │ └── post.py
│ ├── crud/
│ │ ├── init.py
│ │ └── user.py
│ │ └── post.py
│ ├── routers/
│ │ ├── init.py
│ │ └── user.py
│ │ └── post.py
│ ├── utils/
│ │ ├── init.py
│ │ └── auth.py
│ ├── database.py
└── requirements.txt
## License

This project is licensed under the MIT License.

## Contact

For any inquiries or feedback, please contact [godadsamuel@gmail.com](mailto:godadsamuel@gmail.com).
