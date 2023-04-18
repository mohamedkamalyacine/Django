from django.urls import path
from Library.views import welcome, writerInfo

urlpatterns = [
    path('<clientName>', welcome),
    path('<clientName>/<writerName>', writerInfo),
]