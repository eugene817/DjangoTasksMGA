# DjangoTasksMGA

> This is 'tasks manager' app for MGA application

### RUN
- To run this app you need to have docker, docker-compose and Make

1. Simply run 
```bash
make up
```
- Test will run automatically and in case of failure the app won't start
2. Go to the `localhost:8000/` to verify the app launch

### USAGE

#### Register

- First you need to register _new user_, using the endpoints:
`/api/accounts/register/`
with payload:
```json
{
    "username": "user1",
    "email": "test@user1.com",
    "password": "1234",
    "password2": "1234"
}
```
return: **status 201**
```JSON
{
    "message": "User created successfully"
}
```


- Then use the `/api/accounts/token/` with payload:
```json
{
    "username": "user1",
    "password": "1234"
}
```

return: status 200
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9....",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9....."
}
```

#### TASKS

- Example task data
```json
{
    "id": 2,
    "name": "testPostman123",
    "description": null,
    "status": "Nowy",
    "assigned_user": {
        "id": 1,
        "username": "user1"
    },
    "created_at": "2025-02-23T20:29:17.518633Z",
    "updated_at": "2025-02-23T20:29:17.518644Z"
}
```

- The main endpoint is `/api/tasks/{optional: id}`

- You can: GET (all and one), POST, DELETE, PUT

> POST, PUT
> minimal payload is "name":"name"
> to assign user you need to "assigned_user_id": id


- Tasks creation
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"name": "test123", "assigned_user_id": 1}'
```

- Update first task
```bash
curl -X PUT http://localhost:8000/api/tasks/1/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"name": "testPostman4", "assigned_user_id": 1}'
```

- Get all tasks
```bash
curl -X GET http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer <token>"
```

- Get task 1
```bash
curl -X GET http://localhost:8000/api/tasks/1/ \
  -H "Authorization: Bearer <token>"
```

- Delete task number 1
```bash
curl -X DELETE http://localhost:8000/api/tasks/1/ \
  -H "Authorization: Bearer <token>"
```
