from django.urls import path
from .views import email_list

app_name = 'emails'
urlpatterns = [
    path('', email_list, name='sender'),
]
