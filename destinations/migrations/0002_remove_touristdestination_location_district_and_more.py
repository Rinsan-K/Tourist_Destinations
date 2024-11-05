# Generated by Django 5.0.7 on 2024-07-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("destinations", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="touristdestination",
            name="location_district",
        ),
        migrations.RemoveField(
            model_name="touristdestination",
            name="location_state",
        ),
        migrations.AddField(
            model_name="touristdestination",
            name="district",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="touristdestination",
            name="state",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="touristdestination",
            name="google_map_link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="touristdestination",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="touristdestination",
            name="place_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="touristdestination",
            name="weather",
            field=models.CharField(max_length=100),
        ),
    ]
