# Generated by Django 2.2.1 on 2019-05-30 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songList', '0002_playlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='songs',
        ),
        migrations.RemoveField(
            model_name='song',
            name='playlists',
        ),
        migrations.AddField(
            model_name='song',
            name='playlists',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='songList.Playlist'),
            preserve_default=False,
        ),
    ]
