# Generated by Django 2.2.3 on 2019-07-29 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20190729_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='name',
            new_name='simple_name',
        ),
        migrations.AddField(
            model_name='scope',
            name='value',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
