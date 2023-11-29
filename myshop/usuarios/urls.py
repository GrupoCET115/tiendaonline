from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
        path('login_user/',views.login_user,name="login"),
       # path('logout_user',views.logout_user,name="logout"),
        path('register_user',views.register_user,name="register"),
        path('autenticar/',views.autenticar_usuario,name="autenticar"),
        path('enviar_correo/',views.enviar_correo,name='enviar_correo_recuperar_contra'),
        path('recuperar_contra/',views.recuperar_contra,name='recuperar_contra')
    
]