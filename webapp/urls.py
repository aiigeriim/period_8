from django.urls import path

from webapp.views import MainPage, Detail, CreateTask, UpdateTask, DeleteTask

app_name = "webapp"

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),
    path('add/', CreateTask.as_view(), name='create'),
    path('update/<int:pk>/', UpdateTask.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteTask.as_view(), name='delete'),
]