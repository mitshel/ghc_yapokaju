# Generated by Django 2.1.5 on 2019-01-27 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clndr', '0007_auto_20190127_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clndr.Template', verbose_name='шаблон мероприятия'),
        ),
    ]
