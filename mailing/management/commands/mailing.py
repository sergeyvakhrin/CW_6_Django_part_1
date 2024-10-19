import datetime

from django.core.management import BaseCommand

from mailing.models import Mailing, Client


class Command(BaseCommand):

    def handle(self, *args, **options):

        date_time = datetime.datetime.now()
        print("Получили текущую даты и время")
        client_list = []
        print("Создали пустой список клиентов для рассылки")
        mailing_list = Mailing.objects.all()
        print("Получили список объектов рассылок")

        print(vars(mailing_list[4].client_list))

        # for item in mailing_list:
        #     print(item.created_at)

        # a = Mailing.objects.get(pk=data['mailing_id'])

