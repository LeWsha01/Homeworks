from django.contrib.auth.models import Permission, Group
from django.db import migrations
from dashboard import apps


def add_permissions(apps, schema_editor):
    all_permission = Permission.objects.all()
    permission_to_dev = Permission.objects.filter(name__in=['Can view issue', 'Can view project'])
    manager_group = Group.objects.get(name='Manager')
    developer_group = Group.objects.get(name='Developer')

    manager_group.permissions.add(*all_permission)
    developer_group.permissions.add(*permission_to_dev)


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0002_add_groups'),
    ]

    operations = [
        migrations.RunPython(add_permissions)
    ]
