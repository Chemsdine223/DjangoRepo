# Generated by Django 4.1.7 on 2023-04-27 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bank",
            old_name="responsable",
            new_name="admin",
        ),
    ]
