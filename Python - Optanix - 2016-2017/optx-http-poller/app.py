from __future__ import absolute_import
from config.env_config import Env
from tornado.options import define, options
from config.routers import routers
from controller import My404

import os
import tornado.web
import tornado.httpserver
import tornado.ioloop

define("port", default=3000, type=int)
define("env", default='prod', type=str)

_ROOT_PATH = os.path.dirname(__file__)
ROOT_JOIN = lambda sub_dir: os.path.join(_ROOT_PATH, sub_dir)


class Application(tornado.web.Application):
    def __init__(self, router, NotFound=None, **settings):
        default = dict(
            cookie_secret=Env.COOKIE_SEC,
            default_handler_class=NotFound
        )
        super().__init__(handlers=router, **{**default, **settings})
        # service start mongod 
        # self.model = DB(Env)


def main():
    options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(routers, My404, debug=(options.env == 'dev')))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
