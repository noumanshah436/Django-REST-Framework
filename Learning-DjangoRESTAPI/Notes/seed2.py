# python manage.py shell

from faker import Faker
from api.models import Student

# class Student(models.Model):
#     name = models.CharField(max_length=50)
#     roll = models.IntegerField()

fake = Faker()

for i in range(1, 51):
    name = fake.name()
    roll = i  # Assuming roll numbers start from 1 and increment by 1
    student = Student.objects.create(name=name, roll=roll)
    print(f"Created Student: {student.name}, Roll: {student.roll}")
