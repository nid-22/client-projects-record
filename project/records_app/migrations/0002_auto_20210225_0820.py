# Generated by Django 3.1.7 on 2021-02-25 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='businesss_address',
            field=models.CharField(default='work from home', max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(default='work from home', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='project_type',
            field=models.CharField(default='web-based apllication', max_length=75),
            preserve_default=False,
        ),
    ]
