import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import validate_email



class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = "{}__iexact".format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


# Generate filepath for avatar image
def generate_avatar_filepath(instance, filename):
    file_extension = filename.split('.')[-1]
    # return /images/avatars/avatar__user1.jpeg
    return "images/avatars/avatar__{0}.{1}".format(instance.username, file_extension)


class User(AbstractUser):
    first_name = None
    last_name = None
    id = models.UUIDField(verbose_name="User ID", primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.CharField(verbose_name="Full Name", max_length=200, blank=True, default="Anonymous User")
    email = models.EmailField(verbose_name="Email Address", unique=True, blank=False, null=False, validators=[validate_email,],)
    avatar_img = models.ImageField(verbose_name="Avatar Image", upload_to=generate_avatar_filepath, max_length=255, default="images/avatars/default-avatar.jpeg", blank=True,)
    bio = models.TextField(verbose_name="Bio", blank=True,)

    objects = CustomUserManager()

    # Returns the string representation of the object
    def __str__(self):
        return self.username.strip()
    
    # Absolute URL path for User model
    def get_absolute_url(self):
        context_arguments = {
            "username": self.username,
        }
        # return /profile/<username>/
        return reverse(viewname="profile-page", kwargs=context_arguments)
    
    # Settings URL path for User model
    def get_settings_url(self):
        context_arguments = {
            "username": self.username,
        }
        # return /profile/<username>/settings/
        return reverse(viewname="settings-page", kwargs=context_arguments)
    
    class Meta:
        db_table = "uit_share_user"     # Table name in database
        verbose_name_plural = "Users"   # Displaying this name in admin page
        ordering = ["username"]         # Ordered result when querying
