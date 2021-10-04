# SSRG-NDXSAS021-HLNSAN005-RMRSUV002

Capstone project 2021

Install RabbitMQ Server using your distro's package manager.
Initialize the RabbitMQ Server using the command: `sudo systemctl enable rabbitmq-server`
Start the RabbitMQ Server using the command: `sudo systemctl start rabbitmq-server`
start a Celery worker using the command: `celery -A SSRG.celery worker --loglevel=info`

Admin Credentials:
`username: root`
`password: superuser1@`

Packages required:
Django: `pip install django`
Django Crispy Forms: `pip install django-crispy-forms`
Django Widget Tweaks: `pip install django-widget-tweaks`
Celery: `pip install celery`