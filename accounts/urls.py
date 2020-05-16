from django.urls import path,include, re_path
from accounts import views

app_name='accounts'

urlpatterns = [
    path('perfil/', views.dashboard, name='dashboard'),
    path('entrar/', include('django.contrib.auth.urls'), name='login'),
    path('sair/', views.logout_view, name='logout' ),
    path('cadastre-se/', views.register, name='register'),
    path('nova-senha/', views.password_reset, name='reset'),
    re_path(r'^confirmar-nova-senha/(?P<key>\w+)/$', views.password_reset_confirm, name='reset_confirm'),
    path('editar/', views.edit, name='edit'),
    path('editar-senha/', views.edit_senha, name='edit_senha'),
]