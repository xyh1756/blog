# Generated by Django 2.0.7 on 2018-09-18 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0004_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='read',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='read',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]