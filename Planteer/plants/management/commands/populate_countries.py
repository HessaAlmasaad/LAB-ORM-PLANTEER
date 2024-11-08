import requests
from django.core.management.base import BaseCommand
from plants.models import Country  # Adjust 'plants' to your app name if different

class Command(BaseCommand):
    help = 'Populate countries in the database'

    def handle(self, *args, **kwargs):
        url = 'https://restcountries.com/v3.1/all'
        response = requests.get(url)

        if response.status_code == 200:
            countries_data = response.json()
            self.stdout.write(self.style.SUCCESS(f"Fetched {len(countries_data)} countries."))  # Debug message
            for country in countries_data:
                country_name = country.get('name', {}).get('common')
                if country_name:
                    # Check if the country already exists to avoid duplicates
                    Country.objects.get_or_create(name=country_name)
                    self.stdout.write(self.style.SUCCESS(f"Added/Verified country: {country_name}"))  # Debug message
        else:
            self.stdout.write(self.style.ERROR(f"Failed to fetch countries. Status code: {response.status_code}"))
