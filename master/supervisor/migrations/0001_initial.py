# Generated by Django 3.1.7 on 2021-03-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255, verbose_name='Пользователь')),
                ('phone', models.CharField(max_length=255, verbose_name='телефон')),
                ('address', models.CharField(max_length=255, verbose_name='адресс')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
            ],
        ),
    ]
