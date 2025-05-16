from django.utils.translation import gettext_lazy as _


class GroupChoices:
    SUPERUSER = "superuser"
    CUSTOMER = "customer"

    CHOICES = (
        (SUPERUSER, _("Superuser")),
        (CUSTOMER, _("Customer")),
    )
