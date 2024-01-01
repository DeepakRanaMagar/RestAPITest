# Generated by Django 5.0 on 2024-01-01 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='address',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(help_text='Required', max_length=50, unique=True),
        ),
    ]
