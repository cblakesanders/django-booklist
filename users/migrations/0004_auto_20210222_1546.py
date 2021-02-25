# Generated by Django 3.1.5 on 2021-02-22 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_auto_20210127_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='Sam.jpg', upload_to='profile_pics'),
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('acceptingUserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepting', to=settings.AUTH_USER_MODEL)),
                ('requestUserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requesting', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
