# Movies API

## Setup

Clone the project and cd to the project folder

```bash
  git clone git@github.com:harikrishnan-annappilly/movies-backend-flask.git
```

Change directory

```
  cd movies-backend-flask
```

Install dependencies with pip

```
  pip install -r requirements.txt
```

## Populate Sample Data

Populate sample data using below command

```bash
  python populate.py
```

## Running

Run the project using below command

```bash
  python app.py
```

# API Endpoints

#### User Section

| Method | Endpoint  |
| ------ | --------- |
| GET    | /users    |
| POST   | /users    |
| DELETE | /user/:id |

#### Genre Section

| Method | Endpoint   |
| ------ | ---------- |
| GET    | /genres    |
| POST   | /genres    |
| DELETE | /genre/:id |

#### Movie Section

| Method | Endpoint   |
| ------ | ---------- |
| GET    | /movies    |
| POST   | /movies    |
| PUT    | /movie/:id |
| DELETE | /movie/:id |

## User Section

## `GET /users` - Get all Users

##### Request Body - not required

## `POST /users` - Create new User

##### Request Body

```
{
   "username":"user-name",
   "password":"password@123"
}
```

## `POST /login` - Login with User credentials

##### Request Body

```
{
   "username":"user-name",
   "password":"password@123"
}
```

## `DELETE /user/:id` - Delete User with given ID

##### Request Body - not required

---

## Genre Section

## `GET /genres` - Get all Genres

##### Request Body - not required

## `POST /genres` - Create new Genre

##### Request Body

```
{
    "name":"genre-name"
}
```

## `DELETE /genre/:id` - Delete Genre with given ID

##### Request Body - not required

---

## Movie Section

## `GET /movies` - Get all Movies

##### Request Body - not required

## `POST /movies` - Create new Movie

##### Request Body

```
{
    "title":"movie-name",
    "numberInStock": 1,
    "dailyRentalRate":1.1,
    "liked": false,
    "genreId": 1
}
```

## `PUT /movie/:id` - Edit a Movie with given id

##### Request Body

```
{
    "title":"movie-name",
    "numberInStock": 2,
    "dailyRentalRate":2.2,
    "liked": true,
    "genreId": 2
}
```

## `DELETE /movie/:id` - Delete Movie with given ID

##### Request Body - not required

---
