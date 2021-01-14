from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserTerminal(models.Model):
    username = models.CharField(max_length=30, unique=True, verbose_name=_('user'), null=False)
    first_name = models.CharField(max_length=30, null=False, verbose_name=_('first name'))
    last_name = models.CharField(max_length=50, null=False, verbose_name=_('last name'))
    password = models.CharField(max_length=128, verbose_name=_('password '), null=False)
    last_login = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "%s" % self.username()

    class Meta:
        verbose_name = _("user_terminal")
        verbose_name_plural = _("user_terminals")

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

