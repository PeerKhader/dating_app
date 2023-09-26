from django.contrib.auth.views import PasswordResetView

from django.urls import re_path

urlpatterns = [
    re_path(
        'accounts/password_reset/',
        PasswordResetView.as_view(),
        name='password_reset'
    ),
]