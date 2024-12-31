# Generated by Django 5.1.4 on 2024-12-25 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('TotalPerson', models.IntegerField()),
                ('BookingDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categroy_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=15)),
                ('Description', models.TextField()),
                ('Price', models.IntegerField()),
                ('Image', models.ImageField(upload_to='Items/')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Name', to='BaseApp.itemlist')),
            ],
        ),
    ]