# Generated by Django 3.2.4 on 2021-06-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('djangoTest', '0004_delete_hello'),
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
