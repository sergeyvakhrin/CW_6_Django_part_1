from time import sleep

from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'

    def ready(self):
        """ Метод для автоматического запуска рассылки """
        from mailing.services import start
        sleep(2)
        start()
