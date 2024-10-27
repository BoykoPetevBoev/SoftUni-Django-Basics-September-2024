from django.forms import ValidationError
from django.utils.deconstruct import deconstructible
import re

@deconstructible
class LettersOnlyValidator:
    def __call__(self, value):
        if not re.match("^[A-Za-z]+$", value):
            raise ValidationError("Your name must contain letters only!")
        
@deconstructible
class PasscodeValidator:
    def __call__(self, value):
        if len(value) != 6 or not value.isdigit():
            raise ValidationError(f"Your passcode must be exactly 6 digits!")