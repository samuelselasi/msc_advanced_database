# FastAPI App 

## Content

* [About](#about)
* [Directories](#directories)
* [Files](#files)

## About

This repository contains files and folders to
setup the backend of the API.

## Directories

1. [Routers](./routers) -> Contains multiple
folders of different secions of the backend
with their individual CRUD files to allow
growth in the backend.

2. [Services](./services) -> Contains extra
utilised by the backend like email and
allows any future services like payment
gateways that will be integrated into
the backend.

3. [Static](./static) -> Contains static
templates for emails that will be sent
from the application. This allows devs
to create email templates for situations
such as password reset, request for api-
keys or any future emails.


## Files

1. database.py -> Contains info on
database connection.

2. [Exceptions](./exceptions.py) -> Contains responses
to handle errors with the appropriate response codes.

3. [Main](./main.py) -> Contains the routers and
the entire api structure.

4. [Oauth2 Scheme](./oauth2.py) -> Contains the
algorith for authentication.

5. [Schedulers](./schedulers.py) - Contains functions
to schedule background tasks like sending emails in
the background.

6. [Sockets](./sockets.py) -> Contains algorithms
to handle access tokens/ api keys of users logged
in and curent web sessions.

7. [Utils](./utils.py) -> Contains functions that
handle generation and decoding of access tokens
and password reset codes.

8. [Test](./test_main.py) -> Contains unit tests
for the main file to ensure the application is
functioning well.

9. [Script to create database](./create_db.sh) -> Contains
commands to create a PostgreSQL database user, a database
and set appropriate passwords and permissions.

10. config.py -> Contains user passwords
and secured information like PostgreSQL url, user and
password, mailtrap credentials and other environment
variables required for the application to function.

