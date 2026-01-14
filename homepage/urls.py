from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name='main'),
	path('comments/', views.comments, name='comments'),
	path('info/', views.info, name='info')
]
