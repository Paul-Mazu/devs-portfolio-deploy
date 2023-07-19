# Generated by Django 4.2.2 on 2023-07-15 15:03

from django.db import migrations, models
import project.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("body", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ("created",),
            },
        ),
        migrations.CreateModel(
            name="Project",
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
                (
                    "project_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=project.models.project_image_file_path,
                    ),
                ),
                (
                    "short_desc",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "github_link",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "website_link",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
