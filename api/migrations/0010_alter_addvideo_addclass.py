# Generated by Django 3.2.4 on 2021-08-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210819_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addvideo',
            name='addClass',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('11', 11), ('12', 12)], max_length=10),
        ),
    ]
