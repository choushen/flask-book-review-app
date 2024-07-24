# Book Review Web Application

## Overview
This web application allows users to create and manage lists of books and write reviews for the books they've read. Users must register and log in to create or modify lists and write reviews. Frontend is rudimentary but the main idea was to create backend that supports the features of the app. I will revisit the frontend at somepoint.

## Features
- Use of sessions for user management
- Authentication for secure access
- Unique user data management
- User-friendly interface

## Layout
The application features the following pages:
- `welcome.html`: Welcome page
- `completed.html`: List of reviewed books
- `main.html`: Main page for book management
- `login.html` and `registration.html`: User login and registration
- `review.html`: Page for submitting book reviews

## Architecture
The application follows a 3-tier architecture:
1. **Client Tier**: User interface
2. **Application Tier**: Business logic
3. **Data Tier**: Database storage using SQLite

### Key Classes
- **User**: Manages user information and authentication
  - Fields: `id`, `username`, `password`, `email`, `start_date`, `books`
- **Collection**: Manages book information and reviews
  - Fields: `id`, `title`, `description`, `author`, `read`, `review`, `user_id`

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   flask run
   ```


## Improvements
- More responsive styling
- Password hashing
- Update the dependencies



## Usage
1. Register a new user account.
2. Log in with the registered account.
3. Create and manage book lists.
4. Write and view reviews for books.
