from django.forms import ValidationError
from django.utils.deconstruct import deconstructible


def validator_value(value):
    if value.size > 5 * 1024 * 1024:
        raise ValidationError('The file is t0o big')


@deconstructible
class FileSizeValidator:
    def __init__(self, file_size, message=None):
        self.file_size = file_size
        self.message = message
        
    @property
    def message(self):
        return self.__message
    
    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"The file size must be below or equal to {self.file_size}MB"
        else:
            self.__message = value
        
    def __call__(self, value):
        if value.size > self.file_size * 1024 * 1024:
            raise ValidationError(self.message)
            
    