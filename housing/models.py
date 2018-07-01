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


class VacantParcels(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    handle = models.BigIntegerField(primary_key=True,db_column='HANDLE', blank=True )  # Field name made lowercase.
    siteaddr = models.TextField(db_column='SITEADDR', blank=True, null=True)  # Field name made lowercase.
    inside_x = models.FloatField(db_column='INSIDE_X', blank=True, null=True)  # Field name made lowercase.
    inside_y = models.FloatField(db_column='INSIDE_Y', blank=True, null=True)  # Field name made lowercase.
    acres = models.FloatField(db_column='Acres', blank=True, null=True)  # Field name made lowercase.
    handledbl_x = models.BigIntegerField(db_column='HandleDbl_x', blank=True, null=True)  # Field name made lowercase.
    fid_1 = models.BigIntegerField(db_column='FID_1', blank=True, null=True)  # Field name made lowercase.
    objectid_1 = models.BigIntegerField(db_column='OBJECTID_1', blank=True, null=True)  # Field name made lowercase.
    handle_1 = models.BigIntegerField(db_column='HANDLE_1', blank=True, null=True)  # Field name made lowercase.
    siteaddr_1 = models.TextField(db_column='SITEADDR_1', blank=True, null=True)  # Field name made lowercase.
    handle_12 = models.BigIntegerField(db_column='Handle_12', blank=True, null=True)  # Field name made lowercase.
    ownercat = models.TextField(db_column='OwnerCat', blank=True, null=True)  # Field name made lowercase.
    vl_final = models.BigIntegerField(db_column='VL_Final', blank=True, null=True)  # Field name made lowercase.
    vb_final = models.BigIntegerField(db_column='VB_Final', blank=True, null=True)  # Field name made lowercase.
    vl_a = models.BigIntegerField(db_column='VL_A', blank=True, null=True)  # Field name made lowercase.
    vl_b = models.BigIntegerField(db_column='VL_B', blank=True, null=True)  # Field name made lowercase.
    vl_c = models.BigIntegerField(db_column='VL_C', blank=True, null=True)  # Field name made lowercase.
    vl_d = models.BigIntegerField(db_column='VL_D', blank=True, null=True)  # Field name made lowercase.
    vl_e = models.BigIntegerField(db_column='VL_E', blank=True, null=True)  # Field name made lowercase.
    vl_f = models.BigIntegerField(db_column='VL_F', blank=True, null=True)  # Field name made lowercase.
    vb_a = models.BigIntegerField(db_column='VB_A', blank=True, null=True)  # Field name made lowercase.
    vb_b = models.BigIntegerField(db_column='VB_B', blank=True, null=True)  # Field name made lowercase.
    vb_c = models.BigIntegerField(db_column='VB_C', blank=True, null=True)  # Field name made lowercase.
    vb_d = models.BigIntegerField(db_column='VB_D', blank=True, null=True)  # Field name made lowercase.
    vb_e = models.BigIntegerField(db_column='VB_E', blank=True, null=True)  # Field name made lowercase.
    vb_f = models.BigIntegerField(db_column='VB_F', blank=True, null=True)  # Field name made lowercase.
    vb_g = models.BigIntegerField(db_column='VB_G', blank=True, null=True)  # Field name made lowercase.
    vb_h = models.BigIntegerField(db_column='VB_H', blank=True, null=True)  # Field name made lowercase.
    bd_vb17 = models.BigIntegerField(db_column='BD_VB17', blank=True, null=True)  # Field name made lowercase.
    lu1010 = models.BigIntegerField(db_column='LU1010', blank=True, null=True)  # Field name made lowercase.
    prclhasbld = models.BigIntegerField(db_column='PrclHasBld', blank=True, null=True)  # Field name made lowercase.
    prclnobldg = models.BigIntegerField(db_column='PrclNoBldg', blank=True, null=True)  # Field name made lowercase.
    for_vb18 = models.BigIntegerField(db_column='For_VB18', blank=True, null=True)  # Field name made lowercase.
    for_vl18 = models.BigIntegerField(db_column='For_VL18', blank=True, null=True)  # Field name made lowercase.
    lra_vl = models.BigIntegerField(db_column='LRA_VL', blank=True, null=True)  # Field name made lowercase.
    lra_vb = models.BigIntegerField(db_column='LRA_VB', blank=True, null=True)  # Field name made lowercase.
    lra_gl = models.BigIntegerField(db_column='LRA_GL', blank=True, null=True)  # Field name made lowercase.
    dp_s2016 = models.BigIntegerField(db_column='DP_S2016', blank=True, null=True)  # Field name made lowercase.
    bp_s2016 = models.BigIntegerField(db_column='BP_S2016', blank=True, null=True)  # Field name made lowercase.
    op_s2016 = models.BigIntegerField(db_column='OP_S2016', blank=True, null=True)  # Field name made lowercase.
    condstruc = models.BigIntegerField(db_column='CondStruc', blank=True, null=True)  # Field name made lowercase.
    condbu = models.BigIntegerField(db_column='CondBU', blank=True, null=True)  # Field name made lowercase.
    taxbalyear = models.BigIntegerField(db_column='TaxBalYear', blank=True, null=True)  # Field name made lowercase.
    yrstaxdeli = models.BigIntegerField(db_column='YrsTaxDeli', blank=True, null=True)  # Field name made lowercase.
    taxbal = models.FloatField(db_column='TaxBal', blank=True, null=True)  # Field name made lowercase.
    forpropcat = models.BigIntegerField(db_column='ForPropCat', blank=True, null=True)  # Field name made lowercase.
    forbu_10 = models.BigIntegerField(db_column='ForBU_10', blank=True, null=True)  # Field name made lowercase.
    forbu_2 = models.BigIntegerField(db_column='ForBU_2', blank=True, null=True)  # Field name made lowercase.
    forbu_5 = models.BigIntegerField(db_column='ForBU_5', blank=True, null=True)  # Field name made lowercase.
    formc_10 = models.BigIntegerField(db_column='ForMC_10', blank=True, null=True)  # Field name made lowercase.
    formc_2 = models.BigIntegerField(db_column='ForMC_2', blank=True, null=True)  # Field name made lowercase.
    formc_5 = models.BigIntegerField(db_column='ForMC_5', blank=True, null=True)  # Field name made lowercase.
    forvbrp_10 = models.BigIntegerField(db_column='ForVBRP_10', blank=True, null=True)  # Field name made lowercase.
    forvbrp_2 = models.BigIntegerField(db_column='ForVBRP_2', blank=True, null=True)  # Field name made lowercase.
    forvbrp_5 = models.BigIntegerField(db_column='ForVBRP_5', blank=True, null=True)  # Field name made lowercase.
    foryard_10 = models.BigIntegerField(db_column='ForYard_10', blank=True, null=True)  # Field name made lowercase.
    foryard_2 = models.BigIntegerField(db_column='ForYard_2', blank=True, null=True)  # Field name made lowercase.
    foryard_5 = models.BigIntegerField(db_column='ForYard_5', blank=True, null=True)  # Field name made lowercase.
    lra_aqdate = models.TextField(db_column='LRA_AqDate', blank=True, null=True)  # Field name made lowercase.
    lra_enterd = models.TextField(db_column='LRA_EnterD', blank=True, null=True)  # Field name made lowercase.
    lra_aqyear = models.BigIntegerField(db_column='LRA_AqYear', blank=True, null=True)  # Field name made lowercase.
    lra_tenure = models.BigIntegerField(db_column='LRA_Tenure', blank=True, null=True)  # Field name made lowercase.
    lra_usage = models.TextField(db_column='LRA_Usage', blank=True, null=True)  # Field name made lowercase.
    lra_aqtype = models.TextField(db_column='LRA_AqType', blank=True, null=True)  # Field name made lowercase.
    lra_status = models.TextField(db_column='LRA_Status', blank=True, null=True)  # Field name made lowercase.
    td3 = models.BigIntegerField(db_column='TD3', blank=True, null=True)  # Field name made lowercase.
    td5 = models.BigIntegerField(db_column='TD5', blank=True, null=True)  # Field name made lowercase.
    yrsvacant = models.BigIntegerField(db_column='YrsVacant', blank=True, null=True)  # Field name made lowercase.
    bldgscom = models.BigIntegerField(db_column='BldgsCom', blank=True, null=True)  # Field name made lowercase.
    comcat = models.TextField(db_column='ComCat', blank=True, null=True)  # Field name made lowercase.
    comtype = models.BigIntegerField(db_column='ComType', blank=True, null=True)  # Field name made lowercase.
    comgrdflr = models.BigIntegerField(db_column='ComGrdFlr', blank=True, null=True)  # Field name made lowercase.
    comstories = models.TextField(db_column='ComStories', blank=True, null=True)  # Field name made lowercase.
    comyrblt = models.BigIntegerField(db_column='ComYrBlt', blank=True, null=True)  # Field name made lowercase.
    comconst = models.TextField(db_column='ComConst', blank=True, null=True)  # Field name made lowercase.
    comapts = models.BigIntegerField(db_column='ComApts', blank=True, null=True)  # Field name made lowercase.
    bldgsres = models.BigIntegerField(db_column='BldgsRes', blank=True, null=True)  # Field name made lowercase.
    resunits = models.BigIntegerField(db_column='ResUnits', blank=True, null=True)  # Field name made lowercase.
    resocctype = models.TextField(db_column='ResOccType', blank=True, null=True)  # Field name made lowercase.
    resbsmt = models.TextField(db_column='ResBsmt', blank=True, null=True)  # Field name made lowercase.
    resbmfin = models.TextField(db_column='ResBmFin', blank=True, null=True)  # Field name made lowercase.
    resextwall = models.TextField(db_column='ResExtWall', blank=True, null=True)  # Field name made lowercase.
    reslivarea = models.BigIntegerField(db_column='ResLivArea', blank=True, null=True)  # Field name made lowercase.
    resstories = models.TextField(db_column='ResStories', blank=True, null=True)  # Field name made lowercase.
    resfullbat = models.BigIntegerField(db_column='ResFullBat', blank=True, null=True)  # Field name made lowercase.
    reshlfbath = models.BigIntegerField(db_column='ResHlfBath', blank=True, null=True)  # Field name made lowercase.
    resac = models.BigIntegerField(db_column='ResAC', blank=True, null=True)  # Field name made lowercase.
    resacwin = models.BigIntegerField(db_column='ResACwin', blank=True, null=True)  # Field name made lowercase.
    resch = models.BigIntegerField(db_column='ResCH', blank=True, null=True)  # Field name made lowercase.
    resattic = models.BigIntegerField(db_column='ResAttic', blank=True, null=True)  # Field name made lowercase.
    resgarage = models.BigIntegerField(db_column='ResGarage', blank=True, null=True)  # Field name made lowercase.
    resyrblt = models.BigIntegerField(db_column='ResYrBlt', blank=True, null=True)  # Field name made lowercase.
    acres_1 = models.FloatField(db_column='Acres_1', blank=True, null=True)  # Field name made lowercase.
    cityblock = models.FloatField(db_column='CityBlock', blank=True, null=True)  # Field name made lowercase.
    parcel = models.BigIntegerField(db_column='Parcel', blank=True, null=True)  # Field name made lowercase.
    ownercode = models.BigIntegerField(db_column='OwnerCode', blank=True, null=True)  # Field name made lowercase.
    parcelid = models.BigIntegerField(db_column='ParcelID', blank=True, null=True)  # Field name made lowercase.
    lowaddnum = models.BigIntegerField(db_column='LowAddNum', blank=True, null=True)  # Field name made lowercase.
    lowaddsuf = models.TextField(db_column='LowAddSuf', blank=True, null=True)  # Field name made lowercase.
    highaddnum = models.BigIntegerField(db_column='HighAddNum', blank=True, null=True)  # Field name made lowercase.
    highaddsuf = models.TextField(db_column='HighAddSuf', blank=True, null=True)  # Field name made lowercase.
    stpredir = models.TextField(db_column='StPreDir', blank=True, null=True)  # Field name made lowercase.
    stname = models.TextField(db_column='StName', blank=True, null=True)  # Field name made lowercase.
    sttype = models.TextField(db_column='StType', blank=True, null=True)  # Field name made lowercase.
    stsufdir = models.TextField(db_column='StSufDir', blank=True, null=True)  # Field name made lowercase.
    ownername = models.TextField(db_column='OwnerName', blank=True, null=True)  # Field name made lowercase.
    ownername2 = models.TextField(db_column='OwnerName2', blank=True, null=True)  # Field name made lowercase.
    owneraddr = models.TextField(db_column='OwnerAddr', blank=True, null=True)  # Field name made lowercase.
    ownercity = models.TextField(db_column='OwnerCity', blank=True, null=True)  # Field name made lowercase.
    ownerstate = models.TextField(db_column='OwnerState', blank=True, null=True)  # Field name made lowercase.
    ownerzip = models.BigIntegerField(db_column='OwnerZIP', blank=True, null=True)  # Field name made lowercase.
    asrclassco = models.BigIntegerField(db_column='AsrClassCo', blank=True, null=True)  # Field name made lowercase.
    asrlanduse = models.BigIntegerField(db_column='AsrLandUse', blank=True, null=True)  # Field name made lowercase.
    specbusdis = models.BigIntegerField(db_column='SpecBusDis', blank=True, null=True)  # Field name made lowercase.
    specbusd_1 = models.BigIntegerField(db_column='SpecBusD_1', blank=True, null=True)  # Field name made lowercase.
    tifdist = models.BigIntegerField(db_column='TIFDist', blank=True, null=True)  # Field name made lowercase.
    asdland = models.TextField(db_column='AsdLand', blank=True, null=True)  # Field name made lowercase.
    asdimprove = models.TextField(db_column='AsdImprove', blank=True, null=True)  # Field name made lowercase.
    asdtotal = models.TextField(db_column='AsdTotal', blank=True, null=True)  # Field name made lowercase.
    billland = models.TextField(db_column='BillLand', blank=True, null=True)  # Field name made lowercase.
    billimprov = models.TextField(db_column='BillImprov', blank=True, null=True)  # Field name made lowercase.
    billtotal = models.TextField(db_column='BillTotal', blank=True, null=True)  # Field name made lowercase.
    aprland = models.TextField(db_column='AprLand', blank=True, null=True)  # Field name made lowercase.
    costaprimp = models.TextField(db_column='CostAprImp', blank=True, null=True)  # Field name made lowercase.
    cdalanduse = models.BigIntegerField(db_column='CDALandUse', blank=True, null=True)  # Field name made lowercase.
    zoning = models.TextField(db_column='Zoning', blank=True, null=True)  # Field name made lowercase.
    ressalepri = models.BigIntegerField(db_column='ResSalePri', blank=True, null=True)  # Field name made lowercase.
    ressaledat = models.TextField(db_column='ResSaleDat', blank=True, null=True)  # Field name made lowercase.
    vacbldgyea = models.BigIntegerField(db_column='VacBldgYea', blank=True, null=True)  # Field name made lowercase.
    geocityblo = models.FloatField(db_column='GeoCityBlo', blank=True, null=True)  # Field name made lowercase.
    ward10 = models.BigIntegerField(db_column='Ward10', blank=True, null=True)  # Field name made lowercase.
    precinct10 = models.BigIntegerField(db_column='Precinct10', blank=True, null=True)  # Field name made lowercase.
    nbrhd_x = models.BigIntegerField(db_column='Nbrhd_x', blank=True, null=True)  # Field name made lowercase.
    cdadist = models.BigIntegerField(db_column='CDADist', blank=True, null=True)  # Field name made lowercase.
    cdasubdist = models.BigIntegerField(db_column='CDASubDist', blank=True, null=True)  # Field name made lowercase.
    policedist = models.BigIntegerField(db_column='PoliceDist', blank=True, null=True)  # Field name made lowercase.
    censtract1 = models.BigIntegerField(db_column='CensTract1', blank=True, null=True)  # Field name made lowercase.
    censblock1 = models.BigIntegerField(db_column='CensBlock1', blank=True, null=True)  # Field name made lowercase.
    houseconsd = models.BigIntegerField(db_column='HouseConsD', blank=True, null=True)  # Field name made lowercase.
    zip = models.BigIntegerField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase.
    onfloodblo = models.BigIntegerField(db_column='OnFloodBlo', blank=True, null=True)  # Field name made lowercase.
    giscityblo = models.FloatField(db_column='GisCityBLo', blank=True, null=True)  # Field name made lowercase.
    gisparcel = models.BigIntegerField(db_column='GisParcel', blank=True, null=True)  # Field name made lowercase.
    gisownerco = models.BigIntegerField(db_column='GisOwnerCo', blank=True, null=True)  # Field name made lowercase.
    parcel9 = models.BigIntegerField(db_column='Parcel9', blank=True, null=True)  # Field name made lowercase.
    vb_demock = models.BigIntegerField(db_column='VB_DemoCk', blank=True, null=True)  # Field name made lowercase.
    notvacant = models.BigIntegerField(db_column='NOTvacant', blank=True, null=True)  # Field name made lowercase.
    yardchg5_2 = models.BigIntegerField(db_column='YardChg5_2', blank=True, null=True)  # Field name made lowercase.
    handle_13 = models.BigIntegerField(db_column='Handle__13', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    owner = models.TextField(db_column='Owner', blank=True, null=True)  # Field name made lowercase.
    vl_g = models.BigIntegerField(db_column='VL_G', blank=True, null=True)  # Field name made lowercase.
    vaccattxt = models.TextField(db_column='VacCatTxt', blank=True, null=True)  # Field name made lowercase.
    asdttl2 = models.BigIntegerField(db_column='AsdTtl2', blank=True, null=True)  # Field name made lowercase.
    frontage_x = models.FloatField(db_column='Frontage_x', blank=True, null=True)  # Field name made lowercase.
    handledbl_y = models.BigIntegerField(db_column='HandleDbl_y', blank=True, null=True)  # Field name made lowercase.
    frontage_y = models.FloatField(db_column='Frontage_y', blank=True, null=True)  # Field name made lowercase.
    nbrhd_y = models.BigIntegerField(db_column='Nbrhd_y', blank=True, null=True)  # Field name made lowercase.
    asrnbrhd = models.BigIntegerField(db_column='AsrNbrhd', blank=True, null=True)  # Field name made lowercase.
    neigh_field = models.FloatField(db_column='Neigh #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    neighborhood_name = models.TextField(db_column='Neighborhood Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    assessors_neigh = models.FloatField(db_column='Assessors Neigh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vacant_land_sq_ft_price = models.FloatField(db_column='Vacant Land Sq. Ft. Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vacant_vandalized_residential_buildings_per_unit = models.FloatField(db_column='Vacant Vandalized Residential Buildings per Unit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    residential_new_construction = models.FloatField(db_column='Residential New Construction', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    side_lots = models.FloatField(db_column='Side Lots', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    frontage = models.FloatField(blank=True, null=True)
    sqft = models.FloatField(db_column='SqFt', blank=True, null=True)  # Field name made lowercase.
    bldg_price = models.FloatField(blank=True, null=True)
    vacant_price = models.FloatField(blank=True, null=True)
    side_lot_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacant_parcels'
