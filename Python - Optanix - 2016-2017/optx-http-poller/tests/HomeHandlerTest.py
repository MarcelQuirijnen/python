from tornado.testing import AsyncHTTPTestCase
from app import Application
from config.routers import routers


class HomeHandlerTest(AsyncHTTPTestCase):
    def get_app(self):
        self.app = Application(routers, debug=True)
        return self.app

    def test_home_handler(self):
        response = self.fetch('/', method="GET")
        self.assertEqual(response.code, 200)