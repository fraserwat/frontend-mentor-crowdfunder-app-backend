# Generated by Django 4.0.5 on 2022-06-05 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reward', models.IntegerField()),
                ('amount', models.FloatField()),
            ],
        ),
    ]
