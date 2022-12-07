from time import sleep
from celery import shared_task

@shared_task
def send_book(nombre, mail):
    sleep(10)  # Simula operaciones muy pesadas que congelan a Django
    print(
        nombre + " " + mail
    )
