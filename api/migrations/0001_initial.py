# Generated by Django 2.2.17 on 2021-01-22 02:08

import api.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=300)),
                ('criteria', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Not started'), ('2', 'On going'), ('3', 'Done')], default='1', max_length=40)),
                ('estimate', models.IntegerField(validators=[django.core.validators.MinLengthValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsible', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to=api.models.upload_avatar_path)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
