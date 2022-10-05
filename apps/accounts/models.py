from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class AccountManager(BaseUserManager):

    def create_user(self,email,password=None,mobile=None,**other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        other_fields.setdefault('is_active', True)
        user = self.model(email=email,mobile=mobile,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password=None, mobile=None,**other_fields):
        
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_verified', True)

        if other_fields.get('is_verified') is not True:
            raise ValueError(
                'Superuser must be assigned to is_verified=True.')

        if other_fields.get('is_admin') is not True:
            raise ValueError(
                'Superuser must be assigned to is_admin=True.')

        if other_fields.get('is_active') is not True:
            raise ValueError(
                'Superuser must be assigned to is_active=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email,password,mobile, **other_fields)

class Account(AbstractBaseUser,PermissionsMixin):

    username    = models.CharField(_('Username'), max_length=20,unique=True, null=True)
    email       = models.EmailField(_('email address'), unique=True)
    mobile      = PhoneNumberField(null=True)
    is_active   = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    objects = AccountManager() 

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']


    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def is_staff(self):
        return self.is_admin

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'stethoscope@gmail.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.email