# Generated by Django 4.1.3 on 2022-12-14 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fees', '0003_rename_subject_contact_message_alter_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(null=True),
        ),
    ]