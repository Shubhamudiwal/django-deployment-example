import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen =  Faker()

def populate(N = 5):
    for entry  in range(N):
        fake_first_name = fakegen.name().split()[0]
        fake_lat_name = fakegen.name().split()[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_first_name,last_name = fake_lat_name,email = fake_email)[0]

if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Population Complete")
