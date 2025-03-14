from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, \
    MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, ClientListView, \
    ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, AttemptListView, AttemptDetailView, home

app_name = MailingConfig.name

urlpatterns = [
    path('mailing/', cache_page(60)(MailingListView.as_view()), name='mailing_list'),
    path('mailing/<int:pk>/view/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/create/', MailingCreateView.as_view(), name="mailing_create"),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name="mailing_update"),
    path('mailing<int:pk>/delete/', MailingDeleteView.as_view(), name="mailing_delete"),

    path('', home, name='home'),
    path('message/', cache_page(60)(MessageListView.as_view()), name='message_list'),
    path('message/<int:pk>/view/', MessageDetailView.as_view(), name='message_detail'),
    path('message/create/', MessageCreateView.as_view(), name="message_create"),
    path('message/<int:pk>/update/', MessageUpdateView.as_view(), name="message_update"),
    path('message<int:pk>/delete/', MessageDeleteView.as_view(), name="message_delete"),

    path('client/', cache_page(60)(ClientListView.as_view()), name='client_list'),
    path('client/<int:pk>/view/', ClientDetailView.as_view(), name='client_detail'),
    path('client/create/', ClientCreateView.as_view(), name="client_create"),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name="client_update"),
    path('client<int:pk>/delete/', ClientDeleteView.as_view(), name="client_delete"),

    path('attempt/', cache_page(60)(AttemptListView.as_view()), name='attempt_list'),
    path('attempt/<int:pk>/view/', AttemptDetailView.as_view(), name='attempt_detail'),
]