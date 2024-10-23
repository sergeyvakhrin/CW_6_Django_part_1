from django.contrib.auth.views import LoginView
from django.urls import path

from users.apps import UsersConfig
from users.views import logout_view, RegisterView, ProfileView, email_verification, recovery_password, UsersListView, UsersDetailView, UsersUpdateView, UsersDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path("email-confirm/<str:token>/", email_verification, name='email-confirm'),
    path('recovery/', recovery_password, name='recovery'),

    path('usersmailing/', UsersListView.as_view(), name='usersmailing_list'),
    path('usersmailing/<int:pk>/view', UsersDetailView.as_view(), name='usersmailing_detail'),
    path('usersmailing/<int:pk>/update/', UsersUpdateView.as_view(), name='usersmailing_update'),
    path('usersmailing/<int:pk>/delete/', UsersDeleteView.as_view(), name='usersmailing_delete'),
]