from mysite.celery import app
from time import sleep


@app.task
def new_user_task(user):
    sleep(10)
    print("Новый юзер зарегистрировался")
    