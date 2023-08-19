# Generated by Django 4.2.4 on 2023-08-18 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archive", "0003_alter_paper_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="paper",
            name="original_id",
            field=models.CharField(default=0, editable=False, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="paper",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="paper",
            name="publication_date",
            field=models.DateTimeField(),
        ),
    ]