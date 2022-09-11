from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('query/<id>', views.query, name= 'query'),
    path('search', views.search, name='search'),
    path('student', views.student_view, name='student_view'),
    path('add', views.student_create_view, name='student_create_view')
]