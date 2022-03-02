from .views import RegisterView
# , LoginView, UserView, LogoutView

from django.urls import path

urlpatterns = [
    path('register',RegisterView.as_view())
]