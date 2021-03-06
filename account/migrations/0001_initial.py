# Generated by Django 4.0.3 on 2022-03-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact', models.BigIntegerField(unique=True)),
                ('user_role', models.CharField(default='admin', max_length=10)),
                ('is_superuser', models.BooleanField()),
                ('address', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
