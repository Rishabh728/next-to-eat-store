# Generated by Django 5.1.4 on 2024-12-25 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=15)),
                ('Description', models.TextField()),
                ('Rating', models.IntegerField()),
            ],
        ),
    ]
