# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class Grocery(models.Model):
    gid = models.AutoField(primary_key=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    score = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    match_type = models.CharField(max_length=2, blank=True, null=True)
    side = models.CharField(max_length=1, blank=True, null=True)
    x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    match_addr = models.CharField(max_length=135, blank=True, null=True)
    arc_street = models.CharField(max_length=60, blank=True, null=True)
    arc_city = models.CharField(max_length=40, blank=True, null=True)
    arc_state = models.CharField(max_length=20, blank=True, null=True)
    arc_zip = models.CharField(max_length=12, blank=True, null=True)
    store_name = models.CharField(max_length=254, blank=True, null=True)
    street = models.CharField(max_length=254, blank=True, null=True)
    city = models.CharField(max_length=254, blank=True, null=True)
    state = models.CharField(max_length=254, blank=True, null=True)
    zip = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.PointField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grocery'


class PublicHousing(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    loc_name = models.CharField(max_length=14, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    score = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    match_type = models.CharField(max_length=2, blank=True, null=True)
    side = models.CharField(max_length=1, blank=True, null=True)
    x = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    y = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    match_addr = models.CharField(max_length=135, blank=True, null=True)
    arc_addres = models.CharField(max_length=50, blank=True, null=True)
    arc_city = models.CharField(max_length=50, blank=True, null=True)
    arc_state = models.CharField(max_length=50, blank=True, null=True)
    arc_zipcod = models.CharField(max_length=10, blank=True, null=True)
    no = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    mixed_popu = models.CharField(max_length=254, blank=True, null=True)
    street_no = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    street = models.CharField(max_length=254, blank=True, null=True)
    city = models.CharField(max_length=254, blank=True, null=True)
    zip = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    state = models.CharField(max_length=254, blank=True, null=True)
    population = models.CharField(max_length=254, blank=True, null=True)
    wkb_geometry = models.PointField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'public_housing'


class Landmarks(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    st_louis_field = models.CharField(db_column='st__louis_', max_length=254, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    constructi = models.CharField(max_length=254, blank=True, null=True)
    lat_dd = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    long_dd = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    wkb_geometry = models.PointField(srid=900914, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'landmarks'



