
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_file_size(value):
    '''
    to validate that size of file is not to big 
    because of storage issues 
    '''
    max_size = 100 * 1024 * 1024  # 100 MB
    if value.size > max_size:
        raise ValidationError(_('File size cannot exceed 100 MB.'))