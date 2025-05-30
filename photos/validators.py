from typing import Optional

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:

    def __init__(self, max_size: int, message: Optional[str] = None) -> None:
        self.max_size = max_size
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: str):
        if value is None:
            self.__message = f"File size must be less than {self.max_size} MB."
        else:
            self.__message = value

    def __call__(self, value: UploadedFile) -> None:

        if value.size > self.max_size * 1024 * 1024:
            raise ValidationError(self.message)
