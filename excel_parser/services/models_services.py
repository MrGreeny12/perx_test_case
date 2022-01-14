import magic

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ExcelDocumentValidator():
    error_messages = {
     'content_type': "Document of type %(content_type)s are not supported.",
    }

    def __init__(self, content_types=()):
        self.content_types = content_types

    def __call__(self, data):
        if self.content_types:
            content_type = magic.from_buffer(data.read(), mime=True)
            data.seek(0)

            if content_type not in self.content_types:
                params = {'content_type': content_type}
                raise ValidationError(self.error_messages['content_type'],
                                      'content_type', params)

    def __eq__(self, other):
        return self.content_types == other.content_types
