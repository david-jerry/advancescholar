from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    SET_NULL,
    BooleanField,
    CharField,
    DecimalField,
    ForeignKey,
    ManyToManyField,
    OneToOneField,
    PositiveSmallIntegerField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for advancescholar."""

    #: First and last name do not cover name patterns around the globe
    USER_TYPE_CHOICES = (
        (1, 'Student'),
        (2, 'Guardian'),
        (3, 'Academic Staff'),
        (4, 'Non Academic Staff'),
    )
    middle_name = CharField(max_length=255, blank=False)
    user_type = PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    
    # Make firstname, middlename and lastname required for superuser signup
    REQUIRED_FIELDS = ["first_name", "middle_name", "last_name"]
    
    def name(self):
        """Get firstname and lastname to attach as one.

        Returns:
            str: URL for user detail.

        """
        if (self.first_name, self.middle_name, self.last_name):
            name = f"{self.first_name} {self.middle_name}[0] {self.last_name}"
        else:
            name = self.username
        return name

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


