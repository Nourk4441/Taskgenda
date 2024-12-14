# Task Management Django Project

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <https://github.com/Nourk4441/Taskgenda.git>

# Authentication Setup

## Token-Based Authentication

### Overview
This API uses token-based authentication to secure endpoints. Each user receives a unique token upon authentication, which must be sent in the headers of subsequent requests.

### Setup Instructions
1. Register a user (using Django Admin or API).
2. Obtain a token:
   - **POST** `/api-token-auth/`
     - Request body: `{ "username": "<username>", "password": "<password>" }`
     - Response: `{ "token": "<your_token>" }`

3. Use the token to authenticate requests:
   - Add the token to the `Authorization` header:
     ```
     Authorization: Token <your_token>
     ```

### Example Usage
- **POST** `/api-token-auth/`:
  Request:
  ```bash
  curl -X POST -d "username=testuser&password=12345" http://127.0.0.1:8000/api-token-auth/
