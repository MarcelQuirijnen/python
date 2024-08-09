import json
import traceback

from tornado import web

class OptanixException(web.HTTPError):
    pass