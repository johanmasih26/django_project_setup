# Generated by Django 3.2.4 on 2021-06-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoTest', '0005_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('amount', models.IntegerField(max_length=100)),
                ('order_id', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='photo',
        ),
    ]
