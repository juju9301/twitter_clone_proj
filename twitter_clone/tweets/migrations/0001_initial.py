# Generated by Django 2.2.3 on 2019-07-21 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(blank=True, max_length=280, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/request.user.username/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to=settings.AUTH_USER_MODEL)),
                ('users_like', models.ManyToManyField(related_name='tweets_like', to=settings.AUTH_USER_MODEL)),
                ('users_retweet', models.ManyToManyField(related_name='tweets_retweet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
