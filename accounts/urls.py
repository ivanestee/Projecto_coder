from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('curso-form/', views.curso_form, name='CursoForm'),
    path('cursos/', views.cursos, name='cursos'),  # Asociar la URL 'cursos/' a la vista 'cursos'
    path('inicio/', views.inicio, name='inicio'),
    path('curso-form-2/', views.curso_form_2, name='CursoForm2')
]


