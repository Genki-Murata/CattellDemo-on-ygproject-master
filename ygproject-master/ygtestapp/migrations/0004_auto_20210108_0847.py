# Generated by Django 3.1.5 on 2021-01-07 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygtestapp', '0003_cattell_answer_tmp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cattell_answer',
            name='answer',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cattell_answer_tmp',
            name='answer',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]