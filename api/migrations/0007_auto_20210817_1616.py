# Generated by Django 3.2.6 on 2021-08-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210817_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addvideo',
            name='coverPicture',
            field=models.ImageField(null=True, upload_to='static/coverPicture'),
        ),
        migrations.AlterField(
            model_name='addvideo',
            name='video',
            field=models.FileField(upload_to='static/video'),
        ),
    ]
