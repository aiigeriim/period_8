from django.urls import path

from webapp.views import MainPage, Detail

app_name = "webapp"

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),
]