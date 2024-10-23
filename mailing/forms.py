from django.forms import BooleanField, ModelForm
from django import forms
from mailing.models import Mailing, Message, Client


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class MailingForm(StyleMixin, ModelForm):

    # Добавляем отображение календаря при указании даты
    date_of_first_dispatch = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'type': 'datetime-local',
        'class': 'form-control'}),
        label='Дата первой отправки',
        required=True,
        input_formats=['%Y-%m-%d', '%d-%m-%Y']
        )
    # Todo: отображать в форме только принадлежащие пользователю сообщения message_id и клиентов client_list

    # message_id = Message.objects.filter(owner=)

    class Meta:
        model = Mailing
        exclude = ('owner',)


class MessageForm(StyleMixin, ModelForm):

    class Meta:
        model = Message
        exclude = ('owner',)


class ClientForm(StyleMixin, ModelForm):

    class Meta:
        model = Client
        exclude = ('owner',)
