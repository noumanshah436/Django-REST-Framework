# Generated by Django 5.0.7 on 2024-08-02 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '0001_initial'),
        ('utility', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('photograph', models.ImageField(null=True, upload_to='media/images/readers/photographs')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.gender')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utility.region')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reader',
                'verbose_name_plural': 'Readers',
            },
        ),
        migrations.CreateModel(
            name='MarkAsRead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=True)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.blogpost')),
                ('reader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='readers.reader')),
            ],
            options={
                'verbose_name': 'Mark as Reads',
                'verbose_name_plural': 'Mark As Reads',
            },
        ),
    ]
