# Generated by Django 4.2.6 on 2023-10-06 20:21

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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(blank=True, upload_to='profilepics/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('website', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userInfo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
