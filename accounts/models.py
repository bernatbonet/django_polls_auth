from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.core.mail import send_mail
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    '''
    '''
    username = models.CharField(_('username'), unique=True, max_length=15)
    email = models.EmailField(_('email address'), unique=True, max_length=254)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_username(self):
        '''
        Return the username for this User
        '''
        return self.username
    
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space between
        '''
        full_name = '%s %s' %(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user
        '''
        return self.first_name
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email tho this User
        '''
        send_mail(subject, message, from_email, [self.email], *kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    '''
    Create user token object
    '''
    if created:
        Token.objects.create(user=instance, **kwargs)

# chris 5674e8d0c9408476f8b89dee85d4e08003649cfa
# bob 667594d84815c46eea4c38eb9a686010a1e1db66
# new_user 5f05673bd6ab749fe50832633249a201a13acdc5
# admin 93138ba960dfb4ef2eef6b907718ae04400f606a
