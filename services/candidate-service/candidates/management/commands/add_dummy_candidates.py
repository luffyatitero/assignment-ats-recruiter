from django.core.management.base import BaseCommand
from candidates.models import Candidate
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate 10,000 dummy Candidate records'

    def handle(self, *args, **kwargs):
        fake = Faker()
        genders = ['Male', 'Female', 'Other']
        candidates = []
        for i in range(10000):
            gender = random.choice(genders)
            name = fake.name_male() if gender == 'Male' else fake.name_female() if gender == 'Female' else fake.name()
            candidates.append(Candidate(
                name=name,
                age=random.randint(18, 65),
                gender=gender,
                email=fake.unique.email(),
                phone=fake.unique.msisdn()[:15],
            ))
            if (i + 1) % 1000 == 0:
                Candidate.objects.bulk_create(candidates)
                candidates = []
                self.stdout.write(f'Inserted {i + 1} candidates...')
        if candidates:
            Candidate.objects.bulk_create(candidates)
        self.stdout.write(self.style.SUCCESS('Successfully added 10,000 dummy candidates.'))