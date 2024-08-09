from __future__ import absolute_import

import json

from controller.BaseHandler import BaseHandler
from controller.OptanixException import OptanixException


class HomeHandler(BaseHandler):
    def get(self):
        # raise OptanixException()
        return self.finish({
                'status': {
                    'code': self.get_status(),
                    'message': self.get_reason(),
                }
            })