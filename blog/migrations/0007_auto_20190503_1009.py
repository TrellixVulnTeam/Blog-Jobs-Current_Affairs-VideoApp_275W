# Generated by Django 2.1.7 on 2019-05-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190405_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latest',
            name='summary',
        ),
        migrations.AddField(
            model_name='latest',
            name='category',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='latest',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
