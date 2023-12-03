from django.urls import path
from . import views
urlpatterns = [
    path('registration', views.UserRegistrationView.as_view(), name="registration"),
    path('login', views.UserLoginView.as_view(), name="login"),
    path('details', views.UserDetailView.as_view(), name="details"),
    path('update', views.UserUpdateView.as_view(), name="update"),
    path('delete', views.UserDeleteView.as_view(), name="delete"),
    path('logout', views.UserLogoutView.as_view(), name="logout")
]