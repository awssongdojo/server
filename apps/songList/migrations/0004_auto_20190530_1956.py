# Generated by Django 2.2.1 on 2019-05-30 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songList', '0003_auto_20190530_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='playlists',
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='playlist', to='songList.Song'),
            preserve_default=False,
        ),
    ]
