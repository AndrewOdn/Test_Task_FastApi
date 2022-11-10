How to start?
1) start API :  main.py
2) start Celery :  celery -A main.celery worker -l INFO -Q high_priority_tasks
Dependencies -> settings.py
