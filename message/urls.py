from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('', views.message_list, name='message_list'),
    path('send/', views.send_message, name='send_message'),
    path('<int:message_id>/', views.message_detail, name='message_detail'),
    path('<int:message_id>/mark_as_read/', views.mark_as_read, name='mark_as_read'),
    path('<int:message_id>/delete/', views.delete_message, name='delete_message'),
]
