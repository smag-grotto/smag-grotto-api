# Smag Grotto - API v1

## REST API
1. Responses must be JSON.
2. 🔐 indicates that an endpoint requires a valid `authorization` header. An unauthorized request should respond with a 401 error.
3. `?` indicates that a parameter is optional.

## Default Responses

### 400 - Bad Request
For a generic client error:
```json
{
	"message": "Client error."
}
```

### 401 - Unauthorized
For endpoints that require authorization and invalid authorization is given:
```json
{
	"message": "Authorization required."
}
```

### 404 - Not Found
For when a requested file cannot be found or does not exist:
```json
{
	"message": "Resource not found."
}
```

## Endpoints

### Authentication

### `POST /api/signup`
#### Parameters
- `username` - ^\w{3,16}$
- `password` - ^.*$

#### Response (201)
```json
{
	"message": "User created.",
	"user": <string>
}
```
