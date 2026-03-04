# Django Wordle

A minimal Wordle clone implemented with Django and vanilla JavaScript.

## Structure

```text
wordle_django/
├── game/
│   ├── logic.py
│   ├── views.py
│   ├── urls.py
│   ├── words.py
│   ├── words.txt
│   └── templates/game/wordle.html
├── wordle_django/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## Setup

Clone or download this repo, then run these commands from the project root (the folder containing `manage.py`).

### 1. Change into the project directory

```bash
cd wordle_django
```

Ensures you're in the project root so all subsequent commands run in the right place.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Creates an isolated Python environment in `.venv/`, so project dependencies stay separate from your system Python and other projects.

### 3. Activate the virtual environment

```bash
source .venv/bin/activate
```

On Windows (Command Prompt):

```bash
.venv\Scripts\activate
```

On Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

Activates the virtual environment. Your prompt will typically show `(.venv)` when it's active. From here on, `python` and `pip` use the environment’s interpreter and packages.

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

Installs the Python packages listed in `requirements.txt` (including Django) into the virtual environment.

### 5. Apply database migrations

```bash
python manage.py migrate
```

Creates and updates the database tables that Django needs. A SQLite database file (`db.sqlite3`) is created automatically in the project root.

### 6. Start the development server

```bash
python manage.py runserver
```

Starts Django’s development server. Open **http://127.0.0.1:8000/** in your browser to play.

