# Generated by Django 3.0.7 on 2020-06-23 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Patron',
        ),
        migrations.RenameField(
            model_name='patron',
            old_name='useraddress',
            new_name='patronaddress',
        ),
        migrations.RenameField(
            model_name='patron',
            old_name='useremail',
            new_name='patronemail',
        ),
        migrations.RenameField(
            model_name='patron',
            old_name='userfname',
            new_name='patronfname',
        ),
        migrations.RenameField(
            model_name='patron',
            old_name='userlname',
            new_name='patronlname',
        ),
        migrations.RenameField(
            model_name='patron',
            old_name='userphone',
            new_name='patronphone',
        ),
    ]
