from django.urls import path
from . import views
urlpatterns = [
    path('registration', views.UserView.as_view(), name="registration")
]