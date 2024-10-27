import random


from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from blog.models import Blog
from config import settings
from mailing.forms import MailingForm, MessageForm, ClientForm, MailingManagerForm
from mailing.models import Mailing, Message, Client, Attempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mailing
    permission_required = 'mailing.view_mailing'

    # def get_context_data(self, **kwargs):
    #     blogs = Blog.objects.filter(is_published=True).order_by('?')[:3]
    #     mailings = Mailing.objects.all()
    #     mailings_is_published = Mailing.objects.filter(is_published=True)
    #     clients = Client.objects.values('email').distinct()
    #     context = super(MailingListView, self).get_context_data(**kwargs)
    #     context['blog_list'] = blogs
    #     context['mailings_list'] = mailings
    #     context['mailings_is_published'] = mailings_is_published
    #     context['clients_list'] = clients
    #     return context


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'mailing.add_mailing'
    success_url = reverse_lazy('mailing:mailing_list',)

    def form_valid(self, form):
        # Присваиваем объекту Рассылка в поле owner владельца автоматически
        # mailing = form.save()
        # user = self.request.user
        # mailing.owner = user
        # mailing.save()
        form.instance.owner = self.request.user  # так исключается одно обращение к базе
        return super().form_valid(form)

    def get_form_kwargs(self):
        """ Получаем доступ к queryset для фильтрации ManyToMany выводимых данных в форму создания рассылки списка клиентов client_lict
        https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c"""
        kwargs = super(MailingCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'mailing.change_mailing'
    success_url = reverse_lazy('mailing:mailing_list', )

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return MailingForm
        if user.has_perm('mailing.Can_is_published'):
            return MailingManagerForm
        raise PermissionDenied

    def get_form_kwargs(self):
        kwargs = super(MailingUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    permission_required = 'mailing.delete_mailing'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Mailing
    permission_required = 'mailing.view_mailing'

###################################################

def home(request):

    # Низкоуровневое кеширование данных на Главной странице
    if settings.CACHE_ENABLED:
        key_blogs = f'key_blogs_{Blog.objects.filter(is_published=True)}'
        key_mailings = f'key_mailings_{Mailing.objects.all()}'
        key_mailings_is_published = f'key_mailings_is_published_{Mailing.objects.filter(is_published=True)}'
        key_clients = f'key_clients_{Client.objects.values('email').distinct()}'

        # Получаем данные по ключу
        blogs = cache.get(key_blogs)
        mailings = cache.get(key_mailings)
        mailings_is_published = cache.get(key_mailings_is_published)
        clients = cache.get(key_clients)

        if blogs is None or mailings is None or mailings_is_published is None or clients is None:
            blogs = Blog.objects.filter(is_published=True)
            mailings = Mailing.objects.all()
            mailings_is_published = Mailing.objects.filter(is_published=True)
            clients = Client.objects.values('email').distinct()

            # Записываем данные с ключем
            cache.set(key_blogs, blogs)
            cache.set(key_mailings, mailings)
            cache.set(key_mailings_is_published, mailings_is_published)
            cache.set(key_clients, clients)

    else:
        # Если кеширование выключено, получаем данные с базы
        blogs = Blog.objects.filter(is_published=True)
        mailings = Mailing.objects.all()
        mailings_is_published = Mailing.objects.filter(is_published=True)
        clients = Client.objects.values('email').distinct()

    # blogs = Blog.objects.filter(is_published=True)
    # mailings = Mailing.objects.all()
    # mailings_is_published = Mailing.objects.filter(is_published=True)
    # clients = Client.objects.values('email').distinct()
    context = {
        'blog_list': blogs.order_by('?')[:3],
        'mailings_list': mailings,
        'mailings_is_published': mailings_is_published,
        'clients_list': clients
        }
    return render(request, 'mailing/home.html', context)


class MessageListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Message
    permission_required = 'mailing.view_message'


class MessageCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    permission_required = 'mailing.add_message'
    success_url = reverse_lazy('mailing:message_list',)

    def form_valid(self, form):
        # message = form.save()
        # user = self.request.user
        # message.owner = user
        # message.save()
        form.instance.owner = self.request.user  # так исключается одно обращение к базе
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    permission_required = 'mailing.change_message'

    # Для вывода двух форм одновременно
    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     MessageFormset = inlineformset_factory(Message, Mailing, MailingForm, extra=1)
    #     if self.request.method == "POST":
    #         context_data['formset'] = MessageFormset(self.request.POST, instance=self.object)
    #     else:
    #         context_data['formset'] = MessageFormset()
    #     return context_data
    #
    # def form_valid(self, form):
    #     context_data = self.get_context_data()
    #     formset = context_data['formset']
    #     if form.is_valid() and formset.is_valid():
    #         self.object = form.save()
    #         formset.instance = self.object
    #         formset.save()
    #         return super().form_valid(form)
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_success_url(self):
        return reverse('mailing:message_detail', args=[self.kwargs.get('pk')])


class MessageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Message
    permission_required = 'mailing.delete_message'
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Message
    permission_required = 'mailing.view_message'

###########################################

class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Client
    permission_required = 'mailing.view_client'


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    permission_required = 'mailing.add_client'
    success_url = reverse_lazy('mailing:client_list',)

    def form_valid(self, form):
        # client = form.save()
        # user = self.request.user
        # client.owner = user
        # client.save()
        form.instance.owner = self.request.user  # так исключается одно обращение к базе
        return super().form_valid(form)

    def get_form_kwargs(self):
        """ Получаем доступ к queryset для фильтрации выводимых данных в форму
        Метод для проверки уникальности почт в списке клиентов у пользователя
        https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c"""
        kwargs = super(ClientCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    permission_required = 'mailing.change_client'
    success_url = reverse_lazy('mailing:client_list', )

    def get_form_kwargs(self):
        kwargs = super(ClientUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    permission_required = 'mailing.delete_client'
    success_url = reverse_lazy('mailing:client_list')


class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Client
    permission_required = 'mailing.view_client'

###########################################

class AttemptListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Attempt
    permission_required = 'mailing.view_attempt'


class AttemptDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Attempt
    permission_required = 'mailing.view_attempt'


class AttemptCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Attempt
    permission_required = 'mailing.create_attempt'

    def form_valid(self, form):
        # attempt = form.save()
        # user = self.request.user
        # attempt.owner = user
        # attempt.save()
        form.instance.owner = self.request.user  # так исключается одно обращение к базе
        return super().form_valid(form)
