# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Track'
        db.create_table(u'playlists_track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'playlists', ['Track'])

        # Adding model 'Playlist'
        db.create_table(u'playlists_playlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'playlists', ['Playlist'])

        # Adding M2M table for field tracks on 'Playlist'
        m2m_table_name = db.shorten_name(u'playlists_playlist_tracks')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('playlist', models.ForeignKey(orm[u'playlists.playlist'], null=False)),
            ('track', models.ForeignKey(orm[u'playlists.track'], null=False))
        ))
        db.create_unique(m2m_table_name, ['playlist_id', 'track_id'])


    def backwards(self, orm):
        # Deleting model 'Track'
        db.delete_table(u'playlists_track')

        # Deleting model 'Playlist'
        db.delete_table(u'playlists_playlist')

        # Removing M2M table for field tracks on 'Playlist'
        db.delete_table(db.shorten_name(u'playlists_playlist_tracks'))


    models = {
        u'playlists.playlist': {
            'Meta': {'object_name': 'Playlist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tracks': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['playlists.Track']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'playlists.track': {
            'Meta': {'object_name': 'Track'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['playlists']