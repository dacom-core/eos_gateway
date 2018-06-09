from django.core.management.base import BaseCommand

from apps.eos.backend import EosBackend


class Command(BaseCommand):
    def handle(self, *args, **options):
        backend = EosBackend()
        backend.get_actions()
