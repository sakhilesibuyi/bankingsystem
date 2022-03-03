
from unicodedata import name
from rest_framework.authtoken.views import obtain_auth_token


from django.urls import path,re_path
from .views import (
    BankDetailView,
    BranchDetailView,
    BranchView,
    BankView,
     RegisterView,
     LogOutView,
     ClientView
     )

# url patterns to be matched
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register',RegisterView.as_view()),
    path('login',obtain_auth_token, name='api_token_auth'),
    path('logout',LogOutView.as_view(), name="logout-view"),
    path('branches/',BranchView.as_view(), name="branch-lists"),
    path('bank/', BankView.as_view(), name="bank-lists"),
    path('client/',ClientView.as_view(), name="client-lists"),
    re_path(r'^client/(?P<pk>[0-9]+)/', ClientView.as_view(),name="client-detail"), # gets matched when you include the id in the url, the id is expected to be a numeric value
    re_path(r'^bank/(?P<pk>[0-9]+)/', BankDetailView.as_view(), name="bank-detail"),
    re_path(r'^branch/(?P<pk>[0-9]+)/', BranchDetailView.as_view(), name="branch-detail"),

]