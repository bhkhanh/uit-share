from .models import User as uit_share_user
from uitshare_main.helpers import get_all_categories
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import (
    Signup_Form,
    Login_Form,
    PasswordReset_Form,
    PasswordChange_Form,
    SetPassword_Form,
)
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters




# Sign-up/Registration view
class Signup_View(SuccessMessageMixin, CreateView):
    template_name = "user/sign-up.html"
    form_class = Signup_Form
    form_class.use_required_attribute = False
    extra_context = {
        "title": "Sign Up / UIT Share",
        "category_list": get_all_categories,
    }
    success_url = reverse_lazy("login-page")
    success_message = "Congrats! Your new account has been registerd."
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home-page")
        else:
            return super(Signup_View, self).dispatch(request, *args, **kwargs)



# Log-in/Sign-in view
class Login_View(LoginView):
    template_name = "user/log-in.html"
    form_class = Login_Form
    form_class.use_required_attribute = False
    extra_context = {
        "title": "Log In / UIT Share",
        "category_list": get_all_categories,
    }
    redirect_authenticated_user = True



# Log-out view
class Logout_View(LoginRequiredMixin, LogoutView):
    template_name = "user/log-out.html"
    extra_context = {
        "title": "Logged out / UIT Share",
        "category_list": get_all_categories,
    }
    http_method_names = ["post", "options", "get",]
    login_url = reverse_lazy("login-page")



# User Profile view
class Profile_View(LoginRequiredMixin, DetailView):
    template_name = "user/profile.html"
    model = uit_share_user
    context_object_name = "user_detail"
    slug_url_kwarg = "username"
    slug_field = "username"
    
    def get_context_data(self, **kwargs):
        context_arguments = super().get_context_data(**kwargs)
        context_arguments["title"] = self.get_object().username + " / UIT Share"
        context_arguments["category_list"] = get_all_categories
        return context_arguments



# User Settings view
class Settings_View(LoginRequiredMixin, UpdateView):
    template_name = "user/settings.html"
    model = uit_share_user
    context_object_name = "user_detail"
    slug_url_kwarg = "username"
    slug_field = "username"
    fields = ["name", "username", "email", "avatar_img", "bio",]
    login_url = reverse_lazy("login-page")
    success_url = reverse_lazy("home-page")
    
    def get_context_data(self, **kwargs):
        context_arguments = super().get_context_data(**kwargs)
        context_arguments["title"] = "Settings / UIT Share"
        context_arguments["category_list"] = get_all_categories
        return context_arguments
    
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().username != self.request.user.username:
            return redirect("home-page")
        return super(Settings_View, self).dispatch(request, *args, **kwargs)
    



# Class-based password reset views
#   - PasswordResetView sends the mail
#   - PasswordResetDoneView shows a success message for the above
#   - PasswordResetConfirmView checks the link the user clicked and prompts for a new password
#   - PasswordResetCompleteView shows a success message for the above


class PasswordReset_View(PasswordResetView):
    template_name = "user/password-reset-form.html"
    form_class = PasswordReset_Form
    form_class.use_required_attribute = False
    success_url = reverse_lazy("password-reset-done-page")
    email_template_name = "user/password-reset-email-send.html"
    html_email_template_name = None
    subject_template_name = "user/password-reset-subject.txt"
    title = "Password Reset / UIT Share"
    extra_context = {
        "category_list": get_all_categories,
    }


class PasswordResetDone_View(PasswordResetDoneView):
    template_name = "user/password-reset-form-done.html"
    title = "Password Reset / UIT Share"
    extra_context = {
        "category_list": get_all_categories,
    }


class PasswordResetConfirm_View(PasswordResetConfirmView):
    template_name = "user/password-reset-confirm.html"
    form_class = SetPassword_Form
    form_class.use_required_attribute = False
    success_url = reverse_lazy("password-reset-complete-page")
    title = "Password Reset Confirm / UIT Share"
    extra_context = {
        "category_list": get_all_categories,
    }


class PasswordResetComplete_View(PasswordResetCompleteView):
    template_name = "user/password-reset-complete.html"
    title = "Password Reset Complete / UIT Share"
    extra_context = {
        "category_list": get_all_categories,
    }



# Class-based password change views
#   - PasswordChangeView change the current password to new password
#   - PasswordChangeCompleteView shows a success message for the above


class PasswordChange_View(LoginRequiredMixin, PasswordChangeView):
    template_name = "user/password-change-form.html"
    form_class = PasswordChange_Form
    form_class.use_required_attribute = False
    success_url = reverse_lazy("password-change-done-page")
    login_url = reverse_lazy("login-page")
    title = "Password Change / UIT Share"
    extra_context = {
        "category_list": get_all_categories,
    }


class PasswordChangeDone_View(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = "user/password-change-done.html"
    title = "Password Change Successful / UIT Share"
    login_url = reverse_lazy("login-page")
    extra_context = {
        "category_list": get_all_categories,
    }
