from django.urls import path, include, re_path
from django.conf.urls import url
from courses import views
app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.detalhe, name='detalhe'),
]