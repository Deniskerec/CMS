# Generated by Django 5.0.4 on 2024-04-21 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("month", models.IntegerField(max_length=100)),
                ("year", models.IntegerField(max_length=100)),
                ("timestamp", models.DateTimeField()),
                ("amount", models.IntegerField(max_length=100)),
                ("amount_in_cents", models.FloatField(max_length=100)),
                ("ljublana_trips", models.IntegerField(max_length=100)),
                ("est_trips", models.IntegerField(max_length=100)),
            ],
        ),
    ]
