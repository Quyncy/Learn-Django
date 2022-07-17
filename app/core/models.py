"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# die Klasse UserManager bekommt BaseUserManager vererbt
class UserManager(BaseUserManager):
    """Manager for users."""

    # **extra_field  kann extra Argumente besorgen
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:  # leere email
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """"Create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# AbstractBaseUser ist für die authentifizierung
# PermissionsMixin ist für die Erlaubnis und Felder
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    # unique macht die email adresse eindeutig
    # hier wird die Datenbanktabelle User erstellt
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # nur staff kann sich einloggen

    objects = UserManager()

    USERNAME_FIELD= 'email'
