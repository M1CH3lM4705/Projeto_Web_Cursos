from django.urls import path, include, re_path
from django.conf.urls import url
from courses import views
app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.detalhe, name='detalhe'),
    path('<slug:slug>/inscricao/', views.enrollment, name='enrollment'),
    path('<slug:slug>/cancelar-inscricao/', views.undo_enrollment, name='undo_enrollment'),
    path('<slug:slug>/anuncios/', views.anuncio, name='anuncios'),
    path('<slug:slug>/anuncios/<int:pk>/', views.show_announcement, name='show_anuncios'),
    path('<slug:slug>/aulas/', views.lessons, name='lessons'),
    path('<slug:slug>/aulas/<int:pk>/', views.lesson, name='lesson'),
]