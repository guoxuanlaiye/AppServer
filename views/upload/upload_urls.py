from __future__ import unicode_literals
from .upload_views import UploadFileHandle

urls = [
    (r'file', UploadFileHandle)
]