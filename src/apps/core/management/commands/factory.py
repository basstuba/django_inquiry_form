from django.core.management.base import BaseCommand
from apps.core.models import Contact
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate 50 dummy contact records'

    def handle(self, *args, **kwargs):
        fake = Faker('ja_JP')

        for _ in range(50):
            Contact.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                gender=random.choice([1, 2, 3]),
                email=fake.email(),
                tell=fake.phone_number(),
                address=fake.address().replace('\n', ''),
                building=fake.building_name(),
                category=random.randint(1, 5),
                detail=fake.text(max_nb_chars=200)
            )
        self.stdout.write(self.style.SUCCESS('Successfully created 50 dummy contacts.'))
