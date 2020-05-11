# Django REST Framework API

Link to the API on Heroku: https://drf2020.herokuapp.com/api/v1/

It is entirely self describing API: you can find the documentation
for each API endpoint simply by visiting the URL in your browser.


## Using this API you can:

* Create account
* Log in if you already have an account
* Fill your profile
* Read profiles of other users
* Edit your own profile
* Edit any profile if you have staff status


## Technology stack
* Django Framework 3.0.6
* Django REST Framework 3.11.0
* PostgreSQL 12


## Installation
* Create a virtual environment:

On macOS and Linux:
```bash
python3 -m venv venv
```
On Windows:
```bash
py -m venv venv
```

* Switch your virtal environment in the terminal:

On macOS and Linux:
```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```

* Then install all packages you need.

All requirements are stored in requirements.txt.
Use the package manager [pip](https://pip.pypa.io/en/stable/) 
to install by command:

```bash
pip install -r requirements.txt
```

* Add Django Server in Run/Debug Configuration.

* Now you can run your Django Server by command:
```bash
py manage.py runserver
```
and visit http://127.0.0.1:8000/api/v1/

## Documentation

API root view:
![step1](staticfiles/img/readme/1.jpg?raw=true "Title")

User List-Create view:
![step3](staticfiles/img/readme/2.jpg?raw=true "Title")

User List-Create view::
![step4](staticfiles/img/readme/3.jpg?raw=true "Title")

User detail view:
(admin can edit any profile)
![step4](staticfiles/img/readme/4.jpg?raw=true "Title")

User detail view:
(admin can edit any profile)
![step4](staticfiles/img/readme/5.jpg?raw=true "Title")

User detail view:
(user can edit only his own profile)
![step4](staticfiles/img/readme/6.jpg?raw=true "Title")

Login view:
![step4](staticfiles/img/readme/7.jpg?raw=true "Title")


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU](https://choosealicense.com/licenses/gpl-3.0/)