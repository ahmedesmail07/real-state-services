## Real State Services Full Stack Web App

Welcome to the application that best serves the community, through which it will facilitate dealing with private and public bills, all the services required for any citizen and for all groups.

### Built With :

- Django
- Django REST Frame Work
- DB Sqlite
- HTML 5
- CSS
- Java Script
- Boot Strap

## Features Of The App :

1- Fully customized authentication and authorization .

2- Admin (Owner) can control the app from two diffrence admin panels.

3- Fully customized admin panel for only the superusers (Admins).

4- Users can uploading their own forms for all categories.

5- Chat room with channels and websockets (Each user has it's own chat with admin).

6- Real Time Chat.

7- Super effiecient UI.

8- Full api for integration with custom frontend.

## Installation

- First You Need To Have Python In Your OS
- Pip ( PIP is a package manager for Python packages, or modules if you like )

### Follow Then Next Step Carefully :

    1- Cloning The Repo In New Dir (Empty Dir):

```
[git clone](https://github.com/ahmedesmail07/Real-State-Services)


```

2- After Cloning The Repo Create Virtual Environment

```
python -m venv (Enter Your VirtualEnv Name)
```

3- Activate Virtual Environment

```
virtualenv name(Your Venv Name)
```

```
Linux : source name(Your Venv Name)/bin/activate
Windows : name(Your Venv Name)/Scripts/activate

```

4- Install Requirments

```

After setting up your vertualenv just use one command to install all this requirements using the following command :
```

        pip install -r requirements.txt

5- Migrate The Models ( Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema) Using The Following Command :

```
    python manage.py migrate
```

6-Run server in django_project dir (That Contains manage.py file)

```

    python manage.py runserver

```

- Don't Forget To Create A Super User

```

    python manage.py createsuperuser

```
