# Generated by Django 4.0.3 on 2023-03-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
