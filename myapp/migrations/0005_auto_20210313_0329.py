# Generated by Django 3.0.8 on 2021-03-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210313_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='pics',
            field=models.FileField(blank=True, null=True, upload_to='static/'),
        ),
    ]