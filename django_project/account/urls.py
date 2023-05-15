from django.urls import path
from .views import *
urlpatterns = [
    # POP UP Login View
    # path('login/', Login, name='login'),
    path('login_user', LoginUser, name='login_user'),
    path('logout/', LogoutUser, name='logout'),
]
