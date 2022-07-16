"""
Django command fpr wait for database
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ Entrypoint for command."""
        self.stdout.write('Waiting for database')
        # db = False bis wir es bestätigt bekommen, dann db = True
        db_up = False
        while db_up is False:
            try:
                # Wenn db nicht ready ist dann wird eine exception geworfen
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 sec...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))
