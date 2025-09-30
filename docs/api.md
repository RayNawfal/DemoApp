# Api documentation

- [User login and token generation](#user-login-and-token-generation)
- [Current User Profile](#current-user-profile)

## User login and token generation

### Overview

Authenticates a user with their username and password. Returns an access token on successful authentication.

### HTTP request

```bash
POST /token
```

### Request

- Content-Type: `application/x-www-form-urlencoded`
- Body parameters:
    - `username` (string): The user's username.
    - `password` (string): The user's password.

### Response

- **200 OK**: Returns an access token and token type in JSON format.
- **400 Bad Request**: Returned when username or password is incorrect.

### Example 

#### request

```bash
curl -X POST "https://threatscope.com/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=johndoe&password=secret"
```

#### response

```json
{
  "access_token": "johndoe",
  "token_type": "bearer"
}
```

***

## Current User Profile

### Overview

Returns the profile information of the currently authenticated user. 
Requires an OAuth2 bearer token in the `Authorization` header.

### HTTP request

```bash
GET /users/me
```

### Authentication

- Use OAuth2 Bearer token authentication.
- The token is validated to identify the current user.
- Returns **401 Unauthorized** if the token is missing, invalid or expired.

### Request
- No request body.
- Include the authentication token in the request header:
  
    ```
    Authorization: Bearer <access-token>
    ```

### Response

- **200 OK**: Returns the current user's profile information in JSON format.
- **401 Unauthorized**: Returned when authentication fails.

### Example 

```bash
curl -X GET "https://threatscope.com/users/me" -H "Authorization: Bearer <your_access_token>"
```