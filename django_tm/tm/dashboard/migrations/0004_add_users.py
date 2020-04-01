from django.contrib.auth import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.db import migrations
import csv


def add_managers(apps, schema_editor):
    path = '/home/vlad/Documents/python/django_tm/tm/dashboard/migrations/data/managers.csv'
    with open(path) as f:
        developers = []
        reader = csv.DictReader(f, delimiter=',')
        for line in reader:
            d = models.User.objects.create(
                password=make_password(line['password']),
                last_login=timezone.now(),
                is_superuser=bool(line['is_superuser']),
                username=line['username'],
                first_name=line['first_name'],
                last_name=line['last_name'],
                email=line['email'],
                is_staff=bool(line['is_staff'])
            )
            developers.append(d)
        g = models.Group.objects.get(name='Developer')
        g.user_set.set(developers)


def add_developers(apps, schema_editor):
    path = '/home/vlad/Documents/python/django_tm/tm/dashboard/migrations/data/developers.csv'
    with open(path) as q:
        managers = []
        reader = csv.DictReader(q, delimiter=',')
        for line in reader:
            m = models.User.objects.create(
                password=make_password(line['password']),
                last_login=timezone.now(),
                is_superuser=bool(line['is_superuser']),
                username=line['username'],
                first_name=line['first_name'],
                last_name=line['last_name'],
                email=line['email'],
                is_staff=bool(line['is_staff'])
            )
            managers.append(m)
    w = models.Group.objects.get(name='Manager')
    w.user_set.set(managers)


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0003_add_permissions'),
    ]
    operations = [
        migrations.RunPython(add_developers),
        migrations.RunPython(add_managers)
    ]
