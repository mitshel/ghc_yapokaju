# Generated by Django 2.1.5 on 2019-01-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clndr', '0004_restriction_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='event',
            name='restrictions',
            field=models.ManyToManyField(blank=True, to='clndr.Restriction', verbose_name='ограничения'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_by_agreement',
            field=models.BooleanField(default=False, verbose_name='время по договоренности'),
        ),
    ]
