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

    date_of_first_dispatch = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'type': 'datetime-local',
        'class': 'form-control'}),
        label='Дата первой отправки',
        required=True
    )
    datetime_to_start = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'type': 'datetime-local',
        'class': 'form-control'}),
        label='Когда нужно разослать?',
        required=True
    )
    class Meta:
        model = Mailing
        fields = "__all__"


class MessageForm(StyleMixin, ModelForm):

    class Meta:
        model = Message
        fields = "__all__"


class ClientForm(StyleMixin, ModelForm):

    class Meta:
        model = Client
        fields = "__all__"
