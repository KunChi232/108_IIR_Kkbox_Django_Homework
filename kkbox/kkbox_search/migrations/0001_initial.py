# Generated by Django 2.2.3 on 2019-07-22 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kkbox_song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('song_name', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'kkbox_song',
            },
        ),
        migrations.CreateModel(
            name='userlike_record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=True)),
                ('item_id', models.ForeignKey(db_column='item_id', on_delete=django.db.models.deletion.CASCADE, to='kkbox_search.kkbox_song')),
            ],
            options={
                'db_table': 'userlike_record',
            },
        ),
    ]
