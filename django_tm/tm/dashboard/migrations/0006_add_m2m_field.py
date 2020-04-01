from django.db import migrations, models
from django.contrib.auth.models import User
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0005_add_projects_and_issues')


    ]
    operations = [
        migrations.AddField(
            model_name='Project',
            name='user_project',
            field=models.ManyToManyField(
                blank=True,
                related_name='user_project',
                to=User
            ),
        )
    ]
    