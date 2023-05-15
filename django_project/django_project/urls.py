from django.contrib import admin
from django.urls import path, include

from users.views import newsignup , newlogin
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("elec/", include('ElectricityBills.urls')),
    path("gas/", include('GasBills.urls')),
    path("buildings/", include('Buildings.urls')),
    path("water/", include('WaterBills.urls')),
    path("services/", views.services, name='services'),
    path("index/", views.index, name='index'),
    path("contact/", views.contact, name='contact'),
    path("about/", views.about, name='about'),
    path("accounts/", include('allauth.urls')),
    path('chat/', include('room.urls')),
    path("newsignup/",newsignup), 
    path("newlogin/",newlogin,name='newlogin'),
    path("users/",include("users.urls"))
]
"""
END POINTS OF ALL AUTH :
accounts/signup/ [name='account_signup']
accounts/login/ [name='account_login']
accounts/logout/ [name='account_logout']
accounts/password/change/ [name='account_change_password']
accounts/password/set/ [name='account_set_password']
accounts/inactive/ [name='account_inactive']
accounts/email/ [name='account_email']
accounts/confirm-email/ [name='account_email_verification_sent']
accounts/^confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
accounts/password/reset/ [name='account_reset_password']
accounts/password/reset/done/ [name='account_reset_password_done']
accounts/^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
accounts/password/reset/key/done/ [name='account_reset_password_from_key_done']
"""
