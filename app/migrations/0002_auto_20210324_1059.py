# Generated by Django 3.1.7 on 2021-03-24 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdata',
            name='email',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
