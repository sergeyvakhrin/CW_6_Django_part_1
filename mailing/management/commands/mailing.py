import datetime

import pytz
from django.core.management import BaseCommand

from mailing.models import Mailing, Attempt
from mailing.services import do_send_mail


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Словарь, где ключ Объект Рассылка, а значение список Объектов Клиентов - стек для send_mail()
        mailing_client_dict: dict = {}
        # Получили текущую даты и время: ", date_time)
        date_time = datetime.datetime.now(pytz.utc)
        # Получили список объектов рассылок")
        mailing_list = Mailing.objects.all()

        for mailing in mailing_list:
            # Получаем дату последней успешной попытки рассылки
            attempt_date_mailing = Attempt.objects.filter(mailing_id_id=mailing.id).exclude(status="False").order_by('date_last_attempt').last()
            # Проверяем активность рассылки -", mailing.status)
            if mailing.status == 'W':
                # Проверяем наличие успешных попыток -", attempt_list_mailing)
                if attempt_date_mailing is None:
                    # Проверяем дату первой отправки с текущей датой", mailing.date_of_first_dispatch, date_time)
                    if mailing.date_of_first_dispatch <= date_time:
                        mailing_client_dict[mailing] = mailing.client_list.all()
                else:
                    # Сверяем дату последней удачной попытки с периодичностью рассылки
                    if mailing.periodicity == "D":
                        periodicity_date = attempt_date_mailing.date_last_attempt + datetime.timedelta(days=1)
                        if periodicity_date <= date_time:
                            mailing_client_dict[mailing] = mailing.client_list.all()
                    elif mailing.periodicity == "W":
                        periodicity_date = attempt_date_mailing.date_last_attempt + datetime.timedelta(days=7)
                        if periodicity_date <= date_time:
                            mailing_client_dict[mailing] = mailing.client_list.all()
                    elif mailing.periodicity == "M":
                        periodicity_date = attempt_date_mailing.date_last_attempt + datetime.timedelta(days=30)
                        if periodicity_date <= date_time:
                            mailing_client_dict[mailing] = mailing.client_list.all()
        # Передаем полученные данные на отправку
        do_send_mail(mailing_client_dict)
