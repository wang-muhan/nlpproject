from django.urls import path

from . import views

app_name = "dialog"

urlpatterns = [
    path(
        '',
        views.dialog,
        name='dialog'),
]