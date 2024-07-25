# Django Event Countdown Timer

A Django web application that allows users to create events and displays a countdown timer for each upcoming event on the homepage.


## Features

- Create, view, and delete events.
- Countdown timers for each upcoming event.
- List of all upcoming events on the homepage.


## Requirements

- Python 3.x or later
- Django 3.x or later


## Setup Instructions

### 1. Clone the Repository

```sh
 git clone https://github.com/yourusername/django-event-countdown.git
 cd django-event-countdown
```

### 2. Create and Activate a Virtual Environment

```sh
 python -m venv venv
 source venv/Scripts/activate  # On Mac use `venv\bin\activate`
```

### 3. Install Dependencies

```sh
 pip install django
 pip install -r requirements.txt
```

### 4. Apply Migrations

```sh
 python manage.py makemigrations
 python manage.py migrate
```

### 5. Create a Superuser

```sh
 python manage.py createsuperuser
```

### 6. Run Development Server

```sh
 python manage.py runserver
``` 

### 7. Access the Application

```sh
 Open web browser and go to `http://127.0.0.1:8000`.
``` 