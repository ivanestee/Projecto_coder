from django.contrib import admin
from django.urls import path, include
from blognet.views import saludo, probandoTemplate  # Importa las vistas de tu aplicación blognet
from accounts import views as accounts_views  # Importa las vistas de tu aplicación de cuentas
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación de Django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('probando_template/', probandoTemplate, name='probando_template'),
    path('accounts/', include("accounts.urls")),  # Importa las URLs de tu aplicación de cuentas
    path('accounts/register/', accounts_views.register, name='register'),  # Ruta para el registro de cuentas
    path('accounts/profile/', accounts_views.profile, name='profile'),  # Ruta para el perfil de cuentas
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Ruta para el inicio de sesión
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Ruta para cerrar sesión
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),  # Ruta para cambiar la contraseña
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),  # Ruta para confirmar el cambio de contraseña
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Ruta para restablecer la contraseña
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # Ruta para confirmar el restablecimiento de contraseña
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Ruta para confirmar el restablecimiento de contraseña
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Ruta para confirmar el restablecimiento de contraseña
    path('blogs/', include('blogs.urls')),  # Importa las URLs de tu aplicación de blogs
    path('message/', include('message.urls')),  # Importa las URLs de tu aplicación de mensaje
]


