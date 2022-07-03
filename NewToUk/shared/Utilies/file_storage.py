import uuid
from typing import List

from django.core.files.storage import FileSystemStorage

from NewToUk.settings import MEDIA_ROOT


class FileStorage:
    FS = FileSystemStorage(location=MEDIA_ROOT)

    def save(self, file):
        filename = self.FS.save(f"{uuid.uuid4()}_{file.name.replace(' ', '_')}", file)
        return f"{self.FS.url(filename)}"
