# Generated by Django 5.1.2 on 2024-11-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
