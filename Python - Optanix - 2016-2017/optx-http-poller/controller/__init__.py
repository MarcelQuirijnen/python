from __future__ import absolute_import

from controller.BaseHandler import BaseHandler
from controller.OptanixException import OptanixException


class My404(BaseHandler):
    def get(self):
        raise OptanixException(404)


from .HomeHandler import HomeHandler

__all__ = ['HomeHandler', 'My404']
