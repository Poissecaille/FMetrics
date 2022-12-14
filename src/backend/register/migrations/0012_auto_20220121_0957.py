# Generated by Django 3.2.4 on 2022-01-21 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_auto_20220121_0900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followingrequests',
            old_name='receiver',
            new_name='receiver_id',
        ),
        migrations.RenameField(
            model_name='followingrequests',
            old_name='sender',
            new_name='sender_id',
        ),
        migrations.AlterUniqueTogether(
            name='followingrequests',
            unique_together={('sender_id', 'receiver_id')},
        ),
    ]
