# Product-Microservice

My attempt at coding my own microservice full-stack application. Back-end will be created with python and front-end will be created with Vue.js

## Usage

Run `docker-compose up -build` in order to build each service.
You will need to specify a `.env` file with sensitive information such as your mongodb uri, username and password, and any other sensitive information needed to run this app.
To stop the services, run `docker-compose down`. This will stop all services and shut them down. 

## Backend

The backend is currently in development, being built with `flask` using `python`. The database in use here is `MongoDB`. Data persistence will occur using `docker volumes` for the mongodb service. Endpoints will support all CRUD operations as well as possible authentication in the future, time permitting. In the future, testing will also be done to ensure that they work as expected.

## Frontend

The frontend will be built using VueJS. Styling framework is to be decided but will settle with one of the following:

- Vuetify
- Tailwind CSS
- Bootstrap
- Materialize

The frontend will also be dockerized in the future as well.
