# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WorkoutGroup.description'
        db.add_column(u'groups_workoutgroup', 'description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=400, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WorkoutGroup.description'
        db.delete_column(u'groups_workoutgroup', 'description')


    models = {
        u'groupfit.workoutgoal': {
            'Meta': {'object_name': 'WorkoutGoal'},
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'target_date': ('django.db.models.fields.DateField', [], {}),
            'units': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'groups.workoutgroup': {
            'Meta': {'object_name': 'WorkoutGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'goals': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'groups'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['groupfit.WorkoutGoal']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'groups'", 'blank': 'True', 'to': u"orm['tags.Tag']"})
        },
        u'tags.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        }
    }

    complete_apps = ['groups']