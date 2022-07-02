from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(('The Email must be set'))
             
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        if password is not None:
            user.set_password(password)
        else:
            raise ValueError(('The Password must be set'))

        user.save()
        return user