from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from users.views import *
from users.api_views import *
from . import views



urlpatterns = [
    path("api/password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path(
        "api/password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path('api/user/',CustomUserDetailsView().as_view(),name='profile'),
    path('api/registration/',CustomRegisterView().as_view(),name='profile'),
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
    path("users/",include("users.urls")),
    path("api/",include('dj_rest_auth.urls')),
    path('api/registration/', include('dj_rest_auth.registration.urls')),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('dashboard/elec/',views.electricityServices,name="dashboard_elec"),
    path('dashboard/elec/dashelec1/',views.dashelec1,name="dashboard_elec1"),
    path('dashboard/elec/dashelec2/',views.dashelec2,name="dashboard_elec2"),
    path('dashboard/elec/dashelec3/',views.dashelec3,name="dashboard_elec3"),

    
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
