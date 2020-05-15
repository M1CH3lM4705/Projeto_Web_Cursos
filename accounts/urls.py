from django.urls import path,include
from accounts import views

app_name='accounts'

urlpatterns = [
    path('perfil/', views.dashboard, name='dashboard'),
    path('entrar/', include('django.contrib.auth.urls'), name='login'),
    path('sair/', views.logout_view, name='logout' ),
    path('cadastra-se/', views.register, name='register'),
    path('editar/', views.edit, name='edit'),
    path('editar-senha/', views.edit_senha, name='edit_senha'),
]