# Generated by Django 4.2.5 on 2023-09-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0006_projects_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="projects",
            name="category",
            field=models.ManyToManyField(to="resume.category"),
        ),
    ]
