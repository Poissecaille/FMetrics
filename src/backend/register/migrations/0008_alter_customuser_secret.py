# Generated by Django 3.2.4 on 2022-01-19 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_alter_customuser_secret'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='secret',
            field=models.CharField(max_length=36, null=True),
        ),
    ]
