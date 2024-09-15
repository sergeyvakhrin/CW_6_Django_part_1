from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from mailing.models import Mailing, Message
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ("periodicity", 'status', 'datetime_to_start', 'message_id', 'client_list',)
    success_url = reverse_lazy('mailing:mailing_list',)


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ("periodicity", 'status', 'datetime_to_start', 'message_id', 'client_list',)

    def get_success_url(self):
        return reverse('mailing:mailing_detail', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailView(DetailView):
    model = Mailing

###################################################

class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ("...",)
    success_url = reverse_lazy('mailing:message_list',)


class MessageUpdateView(UpdateView):
    model = Message
    fields = ("...",)

    def get_success_url(self):
        return reverse('mailing:message_detail', args=[self.kwargs.get('pk')])



class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailView(DetailView):
    model = Message

###########################################
