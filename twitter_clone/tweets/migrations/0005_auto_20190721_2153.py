# Generated by Django 2.2.3 on 2019-07-21 18:53

from django.db import migrations, models
import tweets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20190721_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=tweets.models.user_directory_path),
        ),
    ]