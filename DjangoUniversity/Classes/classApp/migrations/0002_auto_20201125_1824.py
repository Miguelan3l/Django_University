# Generated by Django 3.1.3 on 2020-11-26 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='CourseNumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='Duration',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='Instructor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='Tittle',
            field=models.CharField(max_length=60),
        ),
    ]
