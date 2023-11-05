from django.urls import path
from . import views


urlpatterns = [
    path("", views.proxy_view, name="proxy")
]
