# Generated by Django 4.2.4 on 2023-08-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archive", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="paper",
            old_name="author",
            new_name="authors",
        ),
        migrations.RenameField(
            model_name="paper",
            old_name="category",
            new_name="categories",
        ),
        migrations.AddField(
            model_name="paper",
            name="publication_date",
            field=models.CharField(default="hello", max_length=511),
            preserve_default=False,
        ),
    ]
