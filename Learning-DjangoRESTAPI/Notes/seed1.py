# python manage.py shell

#  from gs34 models onwards:
# class Student(models.Model):
#     name = models.CharField(max_length=50)
#     roll = models.IntegerField()
#     city = models.CharField(max_length=50)
#     passby = models.CharField(max_length=50)

from api.models import Student

# Creating dummy data
students = [
    {"name": "Alice", "roll": 101, "city": "New York", "passby": "admin"},
    {"name": "Bob", "roll": 102, "city": "Los Angeles", "passby": "admin"},
    {"name": "Charlie Brown", "roll": 103, "city": "Chicago", "passby": "admin"},
    {"name": "David Wilson", "roll": 104, "city": "Houston", "passby": "admin"},
    {"name": "Eve Davis", "roll": 105, "city": "Phoenix", "passby": "admin"},
]

# Saving to the database
for student in students:
    Student.objects.create(**student)

# Verifying that the students were created
for student in Student.objects.all():
    print(student.name, student.roll, student.city, student.passby)
