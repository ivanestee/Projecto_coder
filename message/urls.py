from django.urls import path
from .views import message_list, message_detail, send_message, mark_as_read, delete_message

urlpatterns = [
    path('', message_list, name='message_list'),
    path('<int:message_id>/', message_detail, name='message_detail'),
    path('send/', send_message, name='send_message'),
    path('<int:message_id>/mark_as_read/', mark_as_read, name='mark_as_read'),
    path('<int:message_id>/delete/', delete_message, name='delete_message'),
]
