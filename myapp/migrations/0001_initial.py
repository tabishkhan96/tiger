# Generated by Django 3.0.8 on 2021-03-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mymodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('course', models.CharField(max_length=100)),
                ('msg', models.TextField(max_length=200)),
            ],
        ),
    ]
