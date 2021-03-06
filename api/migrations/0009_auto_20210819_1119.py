# Generated by Django 3.2.4 on 2021-08-19 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_addvideo_subjectcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addvideo',
            name='isUploadedCoverPicture',
        ),
        migrations.AlterField(
            model_name='addvideo',
            name='libraryName',
            field=models.CharField(max_length=31),
        ),
        migrations.AlterField(
            model_name='addvideo',
            name='videoLanguage',
            field=models.CharField(choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Tamil', 'Tamil'), ('Telugu', 'Telugu'), ('Sanskrit', 'Sanskrit'), ('Malayalam', 'Malayalam'), ('Bangali', 'Bangali'), ('Odia', 'Odia'), ('Urdu', 'Urdu'), ('Pali', 'Pali'), ('Marathi', 'Marathi'), ('Kannada', 'Kannada'), ('Parsian', 'Parsian'), ('Prakrit', 'Prakrit')], max_length=11),
        ),
    ]
