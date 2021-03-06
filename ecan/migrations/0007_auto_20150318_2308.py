# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecan', '0006_auto_20150318_0206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Common_Name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('value', models.CharField(max_length=255, null=True, blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('value', models.CharField(max_length=255, null=True, blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='brand',
            name='user',
        ),
        migrations.RemoveField(
            model_name='description',
            name='user',
        ),
        migrations.RemoveField(
            model_name='item',
            name='brand',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.DeleteModel(
            name='Description',
        ),
        migrations.AddField(
            model_name='item',
            name='common_name',
            field=models.ForeignKey(blank=True, to='ecan.Common_Name', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='logo',
            field=models.ForeignKey(blank=True, to='ecan.Logo', null=True),
            preserve_default=True,
        ),
    ]
