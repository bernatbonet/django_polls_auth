from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    '''
    User manager definition
    '''
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        '''
        Create and saves a User with the given email and password
        '''
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        '''
        Create and saves default user
        '''
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        '''
        Create and saves superuser user
        '''
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have a is_superuser=True'))
        
        return self._create_user(email, password, **extra_fields)