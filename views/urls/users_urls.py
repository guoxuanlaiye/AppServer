from __future__ import unicode_literals
from ..views.users_views  import (
    RegistHandle,
    LoginHandle
)


urls = [
    (r'regist', RegistHandle),
    (r'login', LoginHandle)
]