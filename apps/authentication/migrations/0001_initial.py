# Generated by Django 3.2.11 on 2024-01-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArduinoResults',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('cycle_nr', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'sql_results',
                'managed': False,
            },
        ),
    ]
