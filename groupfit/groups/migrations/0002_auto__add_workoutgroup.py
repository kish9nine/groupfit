# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WorkoutGroup'
        db.create_table(u'groups_workoutgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'groups', ['WorkoutGroup'])

        # Adding M2M table for field tags on 'WorkoutGroup'
        m2m_table_name = db.shorten_name(u'groups_workoutgroup_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workoutgroup', models.ForeignKey(orm[u'groups.workoutgroup'], null=False)),
            ('tag', models.ForeignKey(orm[u'tags.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['workoutgroup_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'WorkoutGroup'
        db.delete_table(u'groups_workoutgroup')

        # Removing M2M table for field tags on 'WorkoutGroup'
        db.delete_table(db.shorten_name(u'groups_workoutgroup_tags'))


    models = {
        u'groups.workoutgroup': {
            'Meta': {'object_name': 'WorkoutGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tags.Tag']", 'symmetrical': 'False'})
        },
        u'tags.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        }
    }

    complete_apps = ['groups']