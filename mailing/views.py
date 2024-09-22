from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse

from mailing.forms import MailingForm, MessageForm
from mailing.models import Mailing, Message
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list',)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list', )

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
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list',)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        MessageFormset = inlineformset_factory(Message, Mailing, MailingForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = MessageFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = MessageFormset()
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_success_url(self):
        return reverse('mailing:message_detail', args=[self.kwargs.get('pk')])



class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailView(DetailView):
    model = Message

###########################################
