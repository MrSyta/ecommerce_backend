# Generated by Django 3.1.1 on 2020-09-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('B', 'Biografia'), ('F', 'Fantasy'), ('H', 'Historia'), ('K', 'Komiks'), ('P', 'Poradnik'), ('I', 'Inne')], max_length=1),
        ),
    ]