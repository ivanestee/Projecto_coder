from django.contrib import admin
from django.urls import path
from blognet.views import saludo, probandoTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('probando_template/', probandoTemplate, name='probando_template'),
]
