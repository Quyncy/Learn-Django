"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    # **extra_field  kann extra Argumente besorgen
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


# Abstractbaseuser ist für die authentifizierung
# PermissionsMixin ist für die erlaubnis und Felder
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    # unique macht die email adresse eindeutig
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # nur staff kann sich einloggen

    objects = UserManager()

    USERNAME_FIELD= 'email'
