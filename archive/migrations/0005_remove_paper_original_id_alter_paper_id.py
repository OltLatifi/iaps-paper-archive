# Generated by Django 4.2.4 on 2023-08-18 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archive", "0004_paper_original_id_alter_paper_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="paper",
            name="original_id",
        ),
        migrations.AlterField(
            model_name="paper",
            name="id",
            field=models.CharField(
                editable=False, max_length=255, primary_key=True, serialize=False
            ),
        ),
    ]
