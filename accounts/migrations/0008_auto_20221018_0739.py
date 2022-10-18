# Generated by Django 2.2 on 2022-10-18 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='referral_code',
            field=models.CharField(default='MED35159', max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='reffered_by',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
