# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WorkoutGoal.name'
        db.add_column(u'groupfit_workoutgoal', 'name',
                      self.gf('django.db.models.fields.CharField')(default='CHANGEME', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WorkoutGoal.name'
        db.delete_column(u'groupfit_workoutgoal', 'name')


    models = {
        u'groupfit.workoutgoal': {
            'Meta': {'object_name': 'WorkoutGoal'},
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'target_date': ('django.db.models.fields.DateField', [], {}),
            'units': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['groupfit']