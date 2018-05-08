# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class Lra(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=128, blank=True, null=True)
    record_no = models.IntegerField(blank=True, null=True)
    handle = models.BigIntegerField(blank=True, null=True)
    parcelid = models.BigIntegerField(blank=True, null=True)
    address = models.IntegerField(blank=True, null=True)
    add_suffix = models.CharField(max_length=128, blank=True, null=True)
    direction = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    type = models.CharField(max_length=128, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=128, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    acquisition_dt = models.CharField(max_length=128, blank=True, null=True)
    centerx = models.FloatField(blank=True, null=True)
    centery = models.FloatField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    value_estimated = models.IntegerField(blank=True, null=True)
    value_est_dt = models.CharField(max_length=128, blank=True, null=True)
    entered_date = models.CharField(max_length=128, blank=True, null=True)
    usage = models.CharField(max_length=128, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    property_source = models.CharField(max_length=128, blank=True, null=True)
    purchase_type = models.CharField(max_length=128, blank=True, null=True)
    parcel_status = models.CharField(max_length=128, blank=True, null=True)
    fulladdress = models.CharField(max_length=128, blank=True, null=True)
    wkb_geometry = models.PointField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'lra'
