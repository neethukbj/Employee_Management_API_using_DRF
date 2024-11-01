# Employee Management API

## Objective
This project is a basic REST API designed to manage employees in a company, focusing on CRUD operations, RESTful principles, and authentication.

## API Overview
The API provides the following endpoints for managing employee records:

### API Endpoints
- **Create an Employee**: `POST /api/employees/`
- **List all Employees**: `GET /api/employees/`
- **Retrieve a Single Employee**: `GET /api/employees/{id}/`
- **Update an Employee**: `PUT /api/employees/{id}/`
- **Delete an Employee**: `DELETE /api/employees/{id}/`

### Employee Model
The Employee model contains the following fields:
- `id`: Unique identifier (auto-generated)
- `name`: String, required
- `email`: Email field, required and unique
- `department`: String, optional (e.g., "HR", "Engineering", "Sales")
- `role`: String, optional (e.g., "Manager", "Developer", "Analyst")
- `date_joined`: Date, auto-generated on creation

### Additional Features
- **Validation**: 
  - Ensure email is unique and valid.
  - The name should not be empty.
- **Error Handling**: 
  - Return appropriate HTTP status codes:
    - `201 Created` for successful creation.
    - `404 Not Found` for invalid employee IDs.
    - `400 Bad Request` for validation errors.
    - `204 No Content` for successful deletion.
- **Filtering**: 
  - Allow filtering of employees by department and role (e.g., `GET /api/employees/?department=HR`).
- **Pagination**: 
  - Limit results per page to 10 employees with pagination support (e.g., `GET /api/employees/?page=2`).
- **Authentication**: 
  - Use token-based authentication (JWT or simple token) to secure the endpoints. Only authenticated users should access these endpoints.

## Testing
Basic tests are written to cover each endpoint and edge cases, such as attempting to create an employee with an existing email.

## Instructions

### Authentication
To authenticate, send a `POST` request to the authentication endpoint to obtain a token. Add the token to Postman's Authorization header for secure requests.

### Endpoint Demos
- **Create Employee (POST /api/employees/)**: Demonstrates creating an employee with valid data and handling a duplicate email (400 error).
- **List Employees (GET /api/employees/)**: Show all employees with pagination and filtering by department or role.
- **Retrieve Employee (GET /api/employees/{id}/)**: Fetch a single employee by ID, showing a successful request and a 404 error for non-existent IDs.
- **Update Employee (PUT /api/employees/{id}/)**: Modify an employee’s details and verify the updated response.
- **Delete Employee (DELETE /api/employees/{id}/)**: Delete an employee and confirm with a 204 No Content status.


