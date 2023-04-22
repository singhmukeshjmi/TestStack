# The views used below are normally mapped in the AdminSite instance.
# This URLs file is used to provide a reliable view deployment for test purposes.
# It is also provided as a convenience to those who want to deploy these URLs
# elsewhere.

from accounts import views
from account import views2
# from teststack import views as teststackviews
from django.urls import path


urlpatterns = [
    path("try/", views.tryview, name="tryview"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/", views.PasswordChangeView.as_view(), name="password_change"
        ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
        ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path(
        "profile/",
        views2.mainpage,
        name="mainpage",
    ),
    path(
        "profile/edit/",
        views2.myprofileedit,
        name="profileview",
    ),
    path(
        "profileview/<int:pk>",
        views2.UserUpdateView.as_view(),
        name="profileview",
    ),
    path(
        "profiledetailview/<int:pk>",
        views2.UserDetailView.as_view(fields=['id','password','last_login','is_superuser','username','first_name','last_name','email','is_staff','is_active','date_joined']),
        name="profiledetailview",
    ),
    path(
        "register/",
        views2.UserRegistrationView.as_view(),
        name="userregistration",
    ),
]