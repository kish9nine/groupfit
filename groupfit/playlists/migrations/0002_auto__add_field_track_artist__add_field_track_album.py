# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Track.artist'
        db.add_column(u'playlists_track', 'artist',
                      self.gf('django.db.models.fields.CharField')(default='CHANGEME', max_length=100),
                      keep_default=False)

        # Adding field 'Track.album'
        db.add_column(u'playlists_track', 'album',
                      self.gf('django.db.models.fields.CharField')(default='CHANGEME', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Track.artist'
        db.delete_column(u'playlists_track', 'artist')

        # Deleting field 'Track.album'
        db.delete_column(u'playlists_track', 'album')


    models = {
        u'playlists.playlist': {
            'Meta': {'object_name': 'Playlist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tracks': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['playlists.Track']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'playlists.track': {
            'Meta': {'object_name': 'Track'},
            'album': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['playlists']