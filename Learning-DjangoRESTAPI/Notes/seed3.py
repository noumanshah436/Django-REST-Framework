# python manage.py shell


from faker import Faker
from api.models import Singer, Song  # Replace 'myapp' with the actual app name
import random

fake = Faker()

# Create some singers
for _ in range(10):
    name = fake.name()
    gender = random.choice(['Male', 'Female'])
    singer = Singer(name=name, gender=gender)
    singer.save()

# Create some songs for each singer
singers = Singer.objects.all()
for singer in singers:
    for _ in range(random.randint(1, 5)):  # Each singer has between 1 to 5 songs
        title = fake.sentence(nb_words=3)
        duration = random.randint(120, 300)  # Duration between 2 and 5 minutes
        song = Song(title=title, singer=singer, duration=duration)
        song.save()

print("Seed data created successfully!")
