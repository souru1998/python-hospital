# Generated by Django 4.2.2 on 2023-07-03 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_registrationform_registrationtable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationtable',
            old_name='password',
            new_name='passwords',
        ),
        migrations.RenameField(
            model_name='registrationtable',
            old_name='r_password',
            new_name='re_password',
        ),
    ]
