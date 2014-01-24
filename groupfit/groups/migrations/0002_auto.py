# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field tags on 'WorkoutGroup'
        db.delete_table(db.shorten_name(u'groups_workoutgroup_tags'))


    def backwards(self, orm):
        # Adding M2M table for field tags on 'WorkoutGroup'
        m2m_table_name = db.shorten_name(u'groups_workoutgroup_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workoutgroup', models.ForeignKey(orm[u'groups.workoutgroup'], null=False)),
            ('tag', models.ForeignKey(orm[u'tags.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['workoutgroup_id', 'tag_id'])


    models = {
        u'groups.workoutgroup': {
            'Meta': {'object_name': 'WorkoutGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['groups']