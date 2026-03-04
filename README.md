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

```bash
cd wordle_django
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser to play.

