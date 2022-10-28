# Generated by Django 4.1.2 on 2022-10-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "musicapp",
            "0002_lyrics_delete_lyric_artiste_age_artiste_first_name_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="artiste",
            name="age",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="artiste",
            name="first_name",
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name="artiste",
            name="last_name",
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name="lyrics",
            name="content",
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="lyrics",
            name="song_id",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="song",
            name="artiste_id",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="song",
            name="date_released",
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name="song",
            name="title",
            field=models.CharField(max_length=400),
        ),
    ]