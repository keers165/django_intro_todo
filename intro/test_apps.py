from django.apps import apps
from django.test import TestCase
from .apps import IntroConfig


class TestIntroConfig(TestCase):

    def test_app(self):
        self.assertEqual("intro", IntroConfig.name)
        self.assertEqual("intro", apps.get_app_config("intro").name)