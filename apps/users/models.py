from __future__ import annotations
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.postgres.fields import ArrayField
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    memberships: RelatedManager["Organization", "Membership"]
    
    objects = UserManager()

    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = "email"

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    

class Organization(models.Model):
    memberships: RelatedManager[User, "Membership"]

    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name="organizations", through="Membership")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = ArrayField(
        models.CharField(max_length=50, choices=[("admin", "Admin"), ("member", "Member")]),
        default=list,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    invitation_accepted_at = models.DateTimeField(null=True, blank=True)
    inviteation_expires_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.email} is {self.role} of {self.organization.name}"