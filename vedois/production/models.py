from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class UserTerminal(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True, verbose_name=_('user'), null=False)
    first_name = models.CharField(max_length=30, null=False, verbose_name=_('first name'))
    last_name = models.CharField(max_length=50, null=False, verbose_name=_('last name'))
    password = models.CharField(max_length=30, verbose_name=_('password '), null=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return "%s" % self.get_username()

    class Meta:
        verbose_name = _("user_terminal")
        verbose_name_plural = _("user_terminals")