# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WorkoutGroup.target_date'
        db.add_column(u'groups_workoutgroup', 'target_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 25, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WorkoutGroup.target_date'
        db.delete_column(u'groups_workoutgroup', 'target_date')


    models = {
        u'groups.workoutgroup': {
            'Meta': {'object_name': 'WorkoutGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tags.Tag']", 'symmetrical': 'False'}),
            'target_date': ('django.db.models.fields.DateField', [], {})
        },
        u'tags.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        }
    }

    complete_apps = ['groups']