
from rest_framework.authtoken.views import obtain_auth_token


from django.urls import path,re_path
from .views import (
    BankDetailView,
    BranchDetailView,
    BranchView,
    BankView,
     RegisterView,
     LogOutView
     )

urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',obtain_auth_token, name='api_token_auth'),
    path('logout',LogOutView.as_view()),
    path('branches/',BranchView.as_view()),
    re_path(r'^bank/(?P<pk>[0-9]+)/', BankDetailView.as_view(), name="bank-detail"),
    re_path(r'^branch/(?P<pk>[0-9]+)/', BranchDetailView.as_view(), name="branch-detail"),
    path('bank/', BankView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]