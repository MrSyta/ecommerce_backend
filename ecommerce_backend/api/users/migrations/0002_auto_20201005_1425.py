# Generated by Django 3.1.2 on 2020-10-05 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['date_joined']},
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]
