from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teacher/', views.query_teacher, name='query_teacher'),
    path('test', views.test)
]
