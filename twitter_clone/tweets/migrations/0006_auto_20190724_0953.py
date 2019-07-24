# Generated by Django 2.2.3 on 2019-07-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20190721_2153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.CharField(blank=True, default='', max_length=280),
            preserve_default=False,
        ),
    ]