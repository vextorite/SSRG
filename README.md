# SSRG - A Software Similarity Report Generator

Computer Science Capstone Project 2021
---

Install RabbitMQ Server using your distro's package manager.
Initialize the RabbitMQ Server using the command: `sudo systemctl enable rabbitmq-server`

Start the RabbitMQ Server using the command: `sudo systemctl start rabbitmq-server`

Navigate to Backend/SSRG/ and open 2 terminal instances.
run `python3 manage.py runserver` to run Django in one,

Start a Celery worker using the command: `celery -A SSRG.celery worker --loglevel=info` in the other.

---


Admin Credentials:

`username: root`

`password: superuser1@`

---

Packages required:
Django: `pip install django`

Django Crispy Forms: `pip install django-crispy-forms`

Django Widget Tweaks: `pip install django-widget-tweaks`

Celery: `pip install celery`

fpdf: `pip install fpdf`

fpdf2: `pip install fpdf2`

Pyunpack: `pip install pyunpack`

Dominate: `pip install dominate`
