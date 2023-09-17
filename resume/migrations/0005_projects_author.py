# Generated by Django 4.2.5 on 2023-09-17 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("resume", "0004_alter_contact_options_alter_projects_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="projects",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
