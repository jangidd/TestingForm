# Generated by Django 4.2.13 on 2024-07-06 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Multiform_app", "0012_remove_callback_message_callback_ctcheckbox_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="availabilitydetails", old_name="fritime", new_name="endtime1",
        ),
        migrations.RenameField(
            model_name="availabilitydetails", old_name="montime", new_name="endtime2",
        ),
        migrations.RenameField(
            model_name="availabilitydetails", old_name="sattime", new_name="endtime3",
        ),
        migrations.RenameField(
            model_name="availabilitydetails", old_name="suntime", new_name="endtime4",
        ),
        migrations.RenameField(
            model_name="availabilitydetails",
            old_name="thurstime",
            new_name="starttime1",
        ),
        migrations.RenameField(
            model_name="availabilitydetails", old_name="tuetime", new_name="starttime2",
        ),
        migrations.RenameField(
            model_name="availabilitydetails", old_name="wedtime", new_name="starttime3",
        ),
        migrations.AddField(
            model_name="availabilitydetails",
            name="starttime4",
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
