# Generated by Django 3.1.2 on 2020-12-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20201205_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitymodel',
            name='genre',
            field=models.CharField(choices=[('light', 'Others'), ('info', 'Research'), ('secondary', 'Product')], default='Product', max_length=50),
        ),
    ]
