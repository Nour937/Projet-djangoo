# Generated by Django 4.2 on 2023-04-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
