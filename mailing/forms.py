from django.forms import BooleanField, ModelForm

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
