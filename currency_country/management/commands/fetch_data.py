import json
import sys
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder

from currency_country.models import Country


class Command(BaseCommand):
    help = "Extracting user data to JSON format"

    def handle(self, *args, **options):
        # Get User Data from User Model in monolith
        user_microservice_data = Country.objects.all()
        for country in user_microservice_data:
            data = {
                "model": "Country",
                "id": country.id,
                "country_name": country.country_name,
                "local_currency": country.local_currency,
                "added_on": country.added_on
            }
            # Dumping Data into JSON Format
            json.dump(data, sys.stdout, cls=DjangoJSONEncoder)
            sys.stdout.write("\n")