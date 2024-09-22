from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, \
    MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>/view/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/create/', MailingCreateView.as_view(), name="mailing_create"),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name="mailing_update"),
    path('mailing<int:pk>/delete/', MailingDeleteView.as_view(), name="mailing_delete"),

    path('', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/view/', MessageDetailView.as_view(), name='message_detail'),
    path('message/create/', MessageCreateView.as_view(), name="message_create"),
    path('message/<int:pk>/update/', MessageUpdateView.as_view(), name="message_update"),
    path('message<int:pk>/delete/', MessageDeleteView.as_view(), name="message_delete"),
]