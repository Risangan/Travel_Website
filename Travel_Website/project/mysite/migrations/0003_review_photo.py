# Generated by Django 2.1.2 on 2019-03-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20190221_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='photo',
            field=models.ImageField(blank=True, upload_to='review_photo'),
        ),
    ]