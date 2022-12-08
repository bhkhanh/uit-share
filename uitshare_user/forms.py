from django import forms
from .models import User as uit_share_user
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    UsernameField,
    PasswordResetForm,
    SetPasswordForm,
    PasswordChangeForm,
)
from django.contrib.auth import password_validation
from django.forms import ValidationError


# Sign-up Form
class Signup_Form(UserCreationForm):
    name = forms.CharField(label="Name", required=False,  help_text="Enter your full name here. Default value will be \"Anonymous User\"",)
    password1 = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(), help_text=password_validation.password_validators_help_text_html(),
        error_messages={
            "required": "\"Password\" is required.",
        },
    )
    password2 = forms.CharField(label="Password confirmation", strip=False, widget=forms.PasswordInput(), help_text="Enter the same password as before, for verification.",
        error_messages={
            "required": "\"Password confirmation\" is required.",
        },
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # remove autofocus attribute in the username input from front-end
        self.fields["username"].widget.attrs.pop("autofocus", None)
    
    def clean_username(self):
        username_field = self.cleaned_data.get("username")
        if uit_share_user.objects.filter(username__iexact=username_field).exclude(pk=self.instance.pk).exists():
            raise ValidationError(message="User with the username ‘{}’ already exists, please enter another one.".format(username_field.lower()))
        return username_field.lower()
    
    def clean_email(self):
        email_field = self.cleaned_data.get("email")
        if uit_share_user.objects.filter(email__iexact=email_field).exclude(pk=self.instance.pk).exists():
            raise ValidationError(message="This email address ‘{}’ is already in use, please enter another one.".format(email_field.lower()))
        return email_field.lower()
    
    class Meta:
        model = uit_share_user
        fields = ("name", "username", "email", "password1", "password2",)
        error_messages = {
            "username": {
                "required": "\"Username\" is required.",
            },
            "email": {
                "required": "\"Email address\" is required.",
            }
        }
        help_texts = {
            "email": "Required. Enter a valid email for password reset, newsletter, confirmation link,...",
        }


# User Change Information Form
class UserChange_Form(UserChangeForm):
    class Meta:
        model = uit_share_user
        # fields = "__all__"
        fields = ("name", "username", "email", "avatar_img", "bio",)
        error_messages = {
            "username": {
                "required": "\"Username\" is required.",
            },
            "email": {
                "required": "\"Email address\" is required.",
            }
        }
        help_texts = {
            "email": "Required. Enter a valid email for password reset, newsletter, confirmation link,...",
            "name": "Enter your full name here. Default value will be \"Anonymous\"",
            "avatar_img": "Your profile image.",
            "bio": "Write your introduction here.",
        }



# Log-in Form
class Login_Form(AuthenticationForm):
    username = UsernameField(label="Username", widget=forms.TextInput(attrs={"autofocus": False}),
        error_messages={
            "required": "\"Username\" is required.",
        },
    )
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(),
        error_messages={
            "required": "\"Password\" is required.",
        },
    )
    
    error_messages = {
        "invalid_login": "Invalid username and password, please try again.",
        "inactive": "This account is inactive.",
    }



# Password-Reset Form
class PasswordReset_Form(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(),
        error_messages={
            "required": "\"Email address\" is required.",
        },
    )



class SetPassword_Form(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
        error_messages={
            "required": "\"New password\" is required.",
        },
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(),
        error_messages={
            "required": "\"New password confirmation\" is required.",
        },
    )


class PasswordChange_Form(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old password",
        strip=False,
        widget=forms.PasswordInput(),
        error_messages={
            "required": "\"Current password\" is required.",
        },
    )
    new_password1 = forms.CharField(
        label="New password",
        strip=False,
        widget=forms.PasswordInput(),
        help_text=password_validation.password_validators_help_text_html(),
        error_messages={
            "required": "\"New password\" is required.",
        }
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(),
        error_messages={
            "required": "\"Confirm new password\" is required.",
        }
    )

    error_messages = {
        **SetPasswordForm.error_messages,
        "password_incorrect": "Your current password was entered incorrectly, please enter it again.",
    }