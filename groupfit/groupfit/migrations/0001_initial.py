# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WorkoutGoal'
        db.create_table(u'groupfit_workoutgoal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('activity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('units', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('target_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'groupfit', ['WorkoutGoal'])


    def backwards(self, orm):
        # Deleting model 'WorkoutGoal'
        db.delete_table(u'groupfit_workoutgoal')


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