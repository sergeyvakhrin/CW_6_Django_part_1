from mailing.models import Attempt, Mailing


def do_send_mail(mailing_client_dict):

    count = 0
    for mailing, client_list in mailing_client_dict.items():
        count += 1
        print(count)
        clients = [client.email for client in client_list]
        try:
            print(f'Рассылка: {mailing.message_id.title}\n'
                  f'Сообщение: {mailing.message_id.message}\n'
                  f'Получатели: {clients}')
            server_response = '200'
            attempt_for_create = []
            attempt_for_create.append(Attempt(status=True, server_response=server_response, mailing_id=Mailing.objects.get(pk=mailing.id)))
            Attempt.objects.bulk_create(attempt_for_create)
        except:
            server_response = '404'
            attempt_for_create = []
            attempt_for_create.append(Attempt(status=False, server_response=server_response, mailing_id=Mailing.objects.get(pk=mailing.id)))
            Attempt.objects.bulk_create(attempt_for_create)