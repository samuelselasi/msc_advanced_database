# User Router

## Content

* [About](#about)
* [Files](#files)
* [Endpoints](#endpoints)


## About

This router contains files for handling
endpoints that:

* Reads -> `GET`,
* Creates -> `POST`,
* Updates -> `PUT` or `PATCH` and
* Deletes -> `DELETE`

users of AfriLegal API.


## Files

* [models.py](./models.py): Contains classes with
	                    database tables for
	                    ORM integration.
	                    Classes include:



* [schemas.py](./schemas.py): Contains classes
			      that define schemas
			      for entering into
			      database tables.
			      Classes include:



* [crud.py](./crud.py): Contains functions that
			creates, reads, updates
			and deletes users.
			They include:


* [main.py](./main.py): Contains functions that
			defines enpoints to call
			**CRUD** functions. They
			include:



## Endpoints

* **GET**: `/get_categories`
* **GET**: `/get_category_by_id/{categoryNo}`
* **GET**: `/get_category_by_description/`
* **POST**: `/create_category`
* **PUT**: `/update_category/{categoryNo}`
* **DELETE**: `/delete_category/{categoryNo}`
