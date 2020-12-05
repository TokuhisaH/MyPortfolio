# Generated by Django 3.1.2 on 2020-12-05 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_blogmodel_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitymodel',
            name='trueReserch',
        ),
        migrations.AddField(
            model_name='activitymodel',
            name='genre',
            field=models.CharField(choices=[('light', 'others'), ('info', 'research'), ('secondary', 'product')], max_length=50, null=True),
        ),
    ]
