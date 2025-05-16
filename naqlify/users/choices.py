from django.utils.translation import gettext_lazy as _


class UserStatus:
    """
    User Status Choices
    """

    ACTIVE = "active"
    INACTIVE = "inactive"
    CHOICES = (
        (ACTIVE, _("Active")),
        (INACTIVE, _("Inactive")),
    )


class GenderChoices:
    """
    Gender Choices
    """

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    CHOICES = (
        (MALE, _("Male")),
        (FEMALE, _("Female")),
        (OTHER, _("Other")),
    )


class MarritialStatus:
    """
    Marritial Status Choices
    """

    SINGLE = "single"
    MARRIED = "married"
    DIVORCED = "divorced"
    WIDOWED = "widowed"

    CHOICES = (
        (SINGLE, _("Single")),
        (MARRIED, _("Married")),
        (DIVORCED, _("Divorced")),
        (WIDOWED, _("Widowed")),
    )
