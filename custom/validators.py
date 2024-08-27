
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_file_size(value):
    limit_mb = 30
    if value.size > limit_mb * 1024 * 1024:
        raise ValidationError(f"Max size of file is {limit_mb} MB")
