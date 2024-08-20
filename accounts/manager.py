from typing import Any
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    
   def create_user(self, username, email, password=None, **extra_fields):
        # extra_fields.setdefault("is_staff", False)
        # extra_fields.setdefault("is_superuser", False)
        email = self.normalize_email(email)
        user =  self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    
   def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Admin Users must have an email address")
        # email = email
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_verified', True)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True')
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True')
        # if extra_fields.get('is_verified') is not True:
        #     raise ValueError('Superuser must have is_verified=True')

        print('SuperUser Validation complete')
        return self.create_user(email, password,  **extra_fields)
