# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field goal on 'WorkoutGroup'
        db.delete_table(db.shorten_name(u'groups_workoutgroup_goal'))

        # Adding M2M table for field goals on 'WorkoutGroup'
        m2m_table_name = db.shorten_name(u'groups_workoutgroup_goals')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workoutgroup', models.ForeignKey(orm[u'groups.workoutgroup'], null=False)),
            ('workoutgoal', models.ForeignKey(orm[u'groupfit.workoutgoal'], null=False))
        ))
        db.create_unique(m2m_table_name, ['workoutgroup_id', 'workoutgoal_id'])


    def backwards(self, orm):
        # Adding M2M table for field goal on 'WorkoutGroup'
        m2m_table_name = db.shorten_name(u'groups_workoutgroup_goal')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workoutgroup', models.ForeignKey(orm[u'groups.workoutgroup'], null=False)),
            ('workoutgoal', models.ForeignKey(orm[u'groupfit.workoutgoal'], null=False))
        ))
        db.create_unique(m2m_table_name, ['workoutgroup_id', 'workoutgoal_id'])

        # Removing M2M table for field goals on 'WorkoutGroup'
        db.delete_table(db.shorten_name(u'groups_workoutgroup_goals'))


    models = {
        u'groupfit.workoutgoal': {
            'Meta': {'object_name': 'WorkoutGoal'},
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'target_date': ('django.db.models.fields.DateField', [], {}),
            'units': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'groups.workoutgroup': {
            'Meta': {'object_name': 'WorkoutGroup'},
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