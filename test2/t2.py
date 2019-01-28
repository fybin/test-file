# def test_imp():
#     print('this is test_imp')
#
# test_imp()
# print('this is test2')
# class Base(object):
#     def __init__(self):
#         print('Base')
#
# class Mro(Base):
#     def __init__(self):
#         super(Mro, self).__init__()
#         print('mro')
#
# mro = Mro()
#
# import mistune
# js_content = '\n<script type="text/javascript" src="https://files.cloudcare.cn/home/app/download/download-app.js"></script>\n'
#
# markdown = mistune.Markdown()
# print(markdown(js_content))
#
# print(isinstance(int, type))
# print(int.__class__)
# print(issubclass(type, int.__class__))
import os
import jwt
from typing import Optional, AnyStr,Union
def to_bytes(s: AnyStr, encoding: str='utf-8', errors: str='strict') -> bytes:
    if isinstance(s, str):
        s = s.encode(encoding, errors)
    return s
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNzYXQtbjF2Z1lRZUZwdkFySG5BbURGaXVjNCIsInRpZCI6InRlYW0tYUhHRDFhREQ1UU5zSFZzYTdKVHBBRSIsIm5zIjoiZGVmYXVsdCIsImFpZCI6ImFjbnQtNnI1b1ZoeUVQd0dZVUhSa2hNUmVBTSIsIm1rIjoid2ViIiwiaWF0IjoxNTQ4MzE3MjU5fQ.v9umBEG6X3WyEJJ5wbNId75APZAxc06mGSCs7fORlVA
token = to_bytes('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNzYXQtbjF2Z1lRZUZwdkFySG5BbURGaXVjNCIsInRpZCI6InRlYW0tYUhHRDFhREQ1UU5zSFZzYTdKVHBBRSIsIm5zIjoiZGVmYXVsdCIsImFpZCI6ImFjbnQtNnI1b1ZoeUVQd0dZVUhSa2hNUmVBTSIsIm1rIjoid2ViIiwiaWF0IjoxNTQ4MzE3MjU5fQ.v9umBEG6X3WyEJJ5wbNId75APZAxc06mGSCs7fORlVA')

_basedir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_basedir, 'jwt_rsa_public.pem'), 'r') as f:
    _public_key = to_bytes(f.read())

def jwt_decode(text: AnyStr) -> Union[AnyStr, None]:
    """
    success:
    {'account': {'id': 'acnt-1bd71821-8994-4087-ad0a-5cdb8cc25c24',
                 'namespace': 'default'},
     'team': {'id': 'team-e8b0812a-13cf-4d2e-a2e8-b1d6b2e578b1',
              'isSelfTeam': False,
              'isDefault': True,
              'isAdmin': False},
     'extra': {'authTokenId': 'csat-brLxyfH4uM1fqJc2BNtMpQ',
              'authTokenMarker': 'web'},
     'iat': 1547188665}

    failed:
    raise exc
    """
    return jwt.decode(text, _public_key, algorithms=['RS256'])

_token = jwt_decode(token)
print(_token)