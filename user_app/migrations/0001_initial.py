# Generated by Django 4.0.4 on 2024-02-01 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('card', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'users',
            },
        ),
    ]
