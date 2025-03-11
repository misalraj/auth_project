# Django Authentication API

This project implements a Django-based authentication system with cookie-based authentication. It includes user registration, login, logout, and a protected endpoint to retrieve the logged-in user's details. The API is documented using Swagger, and security measures like CSRF protection and secure cookies are implemented.

---

## Features

- User registration with email and password.
- Email verification using OTP (One-Time Password).
- User login with cookie-based authentication.
- Protected endpoint to fetch logged-in user details.
- Logout functionality to clear authentication cookies.
- Swagger API documentation with automatic CSRF token generation.
- Secure cookies with `HttpOnly` and `Secure` flags.

---

## Requirements

- Python 3.8+
- Django 4.2
- Django REST Framework (DRF)
- drf-yasg (for Swagger documentation)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd auth_project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python3 manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`.

---

## API Endpoints

### Swagger Documentation

- Access Swagger UI at: `http://127.0.0.1:8000/swagger/`

### Available Endpoints

1. **User Registration**
   - **POST** `/api/register/`
   - Request Body:
     ```json
     {
       "email": "user@example.com",
       "password": "securepassword123"
     }
     ```

2. **User Registration Verification**
   - **POST** `/api/register/verify/`
   - Request Body:
     ```json
     {
       "email": "user@example.com",
       "otp": "123456"
     }
     ```

3. **User Login**
   - **POST** `/api/login/`
   - Request Body:
     ```json
     {
       "email": "user@example.com",
       "password": "securepassword123"
     }
     ```

4. **User Details**
   - **GET** `/api/me/`
   - Requires authentication.

5. **User Logout**
   - **POST** `/api/logout/`
   - Clears the authentication cookie.

---

## Testing the API

1. Open Swagger UI at `http://127.0.0.1:8000/swagger/`.
2. Use the `/api/register/` endpoint to register a new user.
3. Verify the user using the `/api/register/verify/` endpoint.
4. Log in using the `/api/login/` endpoint. This will set an `auth_token` cookie.
5. Access the `/api/me/` endpoint to fetch the logged-in user's details.
6. Log out using the `/api/logout/` endpoint.

---

## Security Measures

- **CSRF Protection**: Enabled for all requests. Swagger automatically generates a CSRF token.
- **Secure Cookies**: Authentication cookies are marked as `HttpOnly` and `Secure`.

---

## Dependencies

The project uses the following dependencies:

- Django
- Django REST Framework (DRF)
- drf-yasg (for Swagger documentation)

See `requirements.txt` for the complete list.

---

## Commit History

The project includes a proper commit history to track progress. You can view the commits using:

```bash
git log
```

---