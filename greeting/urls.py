from django.urls import path
from greeting.views import greeting

urlpatterns = [
    path('<name>', greeting),
]
