import uuid
from typing import List

from django.core.files.storage import FileSystemStorage

from NewToUk.settings import MEDIA_ROOT


class FileStorage:
    FS = FileSystemStorage(location=MEDIA_ROOT)

    def save(self, file):
        filename = self.FS.save(f"{uuid.uuid4()}_{file.name.replace(' ', '_')}", file)
        return f"{self.FS.url(filename)}"

    @staticmethod
    def get_files(request) -> List:
        stop: bool = False
        count: int = 1
        files: List = []
        while not stop:
            try:
                file = request.data[f"image{count}"]
                files.append(file)
            except KeyError:
                stop = True
        return files
