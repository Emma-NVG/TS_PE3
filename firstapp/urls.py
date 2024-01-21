# firstapp/urls.py
from django.urls import path
from .views import submit_message, get_messages, test_responses

urlpatterns = [
    path('submit_message/', submit_message, name='submit_message'),
    path('get_messages/', get_messages, name='get_messages'),
    path('test_responses/', test_responses, name='test_responses'),
]
