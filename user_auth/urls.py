from django.urls import path
from . import views
urlpatterns = [
    path('registration', views.UserRegistrationView.as_view(), name="registration"),
    path('login', views.UserLoginView.as_view(), name="login"),
    path('details', views.UserView.as_view())
]