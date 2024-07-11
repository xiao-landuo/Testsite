from mysite.celery import app
from time import sleep


@app.task
def new_user_task(user_email):
    sleep(10)
    print(f"Новый юзер {user_email} зарегистрировался")
    