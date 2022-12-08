from django.urls import path
from .views import (
    Signup_View,
    Login_View,
    Logout_View,
    Profile_View,
    Settings_View,
    PasswordChange_View,
    PasswordChangeDone_View,
    PasswordReset_View,
    PasswordResetDone_View,
    PasswordResetConfirm_View,
    PasswordResetComplete_View,
)


urlpatterns = [
    path(route="sign-up/", view=Signup_View.as_view(), name="signup-page"),
    path(route="log-in/", view=Login_View.as_view(), name="login-page"),
    path(route="log-out/", view=Logout_View.as_view(), name="logout-page"),
    path(route="password-reset/", view=PasswordReset_View.as_view(html_email_template_name="user/password-reset-email-send.html"), name="password-reset-page"),
    path(route="password-reset/done/", view=PasswordResetDone_View.as_view(), name="password-reset-done-page"),
    path(route="password-reset/confirm/<uidb64>/<token>/", view=PasswordResetConfirm_View.as_view(), name="password-reset-confirmation-page"),
    path(route="password-reset/complete/", view=PasswordResetComplete_View.as_view(), name="password-reset-complete-page"),
    path(route="profile/<username>/", view=Profile_View.as_view(), name="profile-page"),
    path(route="profile/<username>/settings/", view=Settings_View.as_view(), name="settings-page"),
    path(route="password-change/", view=PasswordChange_View.as_view(), name="password-change-page"),
    path(route="password-change/done/", view=PasswordChangeDone_View.as_view(), name="password-change-done-page"),
]