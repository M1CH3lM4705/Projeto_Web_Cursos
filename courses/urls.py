from django.urls import path, include, re_path
from django.conf.urls import url
from courses import views
app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.detalhe, name='detalhe'),
    path('<slug:slug>/inscricao/', views.enrollment, name='enrollment'),
    path('<slug:slug>/anuncios/', views.anuncio, name='anuncios'),
]