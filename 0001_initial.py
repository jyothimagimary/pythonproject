# Generated by Django 4.2.2 on 2023-06-09 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=2550)),
                ('address', models.CharField(max_length=2550)),
                ('contact', models.IntegerField()),
                ('email', models.CharField(max_length=2550)),
                ('objective', models.CharField(max_length=4550)),
                ('Skills', models.CharField(max_length=2550)),
            ],
        ),
    ]
