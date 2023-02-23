import json
import sys
import logging

from dateutil import parser
from django.core.management.base import BaseCommand

from currency_country.models import Country

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Populating User data obtained in JSON from Monolith."

    def handle(self, *args, **options):
        for line in sys.stdin:
            data = json.loads(line)

            # Populating User Model
            if data["model"] == "Country":
                country= Country(
                    id=data["id"],
                    country_name=data["country_name"],
                    local_currency=data["local_currency"],
                    added_on=parser.parse(data["added_on"]),
                )
                country.save()
                logger.debug("User populated:{}".format(country.id))