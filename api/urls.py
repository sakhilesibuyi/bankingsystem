from .views import *
# , UserView, 

from django.urls import path

urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('logout',LogOutView.as_view()),
    path('branches/',BranchView.as_view()),

]