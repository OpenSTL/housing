from django.conf import settings
from django.shortcuts import render
from django.contrib.gis.geos import Polygon
from django.core.serializers import serialize 
from django.http import HttpResponseRedirect, HttpResponse , JsonResponse, Http404
from django.urls import reverse
#from models import BuildingFootprints,Landmarks,PublicHousing,VacantParcels
from models import Landmarks,PublicHousing,VacantParcels
import json



def index(request):
    return render(request, 'index.html' )
    
def vacant_parcels_byId(id):
    VacantParcelJson = serialize('geojson',VacantParcels.objects.get(pk=id), geometry_field='geom',fields=('siteaddr', 'tifdist','acres' ))
    JsonResponse(json.loads(VacantParcelJson))

def homer(request):
    GET = request.GET
    plotChoice = GET['plotChoice'] 
    userQuery = VacantParcels.objects.filter(acres__gt=GET['minAcers'],nbrhd=GET['nbrhd'])
    if plotChoice == 'prevBuild':
        userQuery = userQuery.filter(price__bldg_price__gt=GET['minprice'],price__bldg_price__lt=GET['maxprice'])
    elif plotChoice == 'currBuild':
        userQuery = userQuery.filter(price__new_construction_price__gt=GET['minprice'], price__new_construction_price__lt=GET['maxprice'])
    elif plotChoice == 'noBuild':
       userQuery = userQuery.filter(price__vacant_lot_price__gt=GET['minprice'],price__vacant_lot_price__lt=GET['maxprice'])
    else: 
        userQuery = userQuery.filter(price__side_lot_price__gt=GET['minprice'], price__side_lot_price__lt=GET['maxprice'])
    print userQuery
    resultJson = serialize('geojson',userQuery.order_by(price__outcomes), geometry_field='geom',fields=('siteaddr', 'tifdist','acres' ))
    if  resultJson:
        return JsonResponse(json.loads(resultJson))
    else:
        return Http404 

def publichousing(request):
    publichousingJson = serialize('geojson',PublicHousing.objects.all(), geometry_field='wkb_geometry',fields=('id','handle',))
    if publichousingJson: 
        result = json.loads(publichousingJson)
        return  JsonResponse(result) 
    else:
        return Http404

def publichousing_byId(id):
        parcelJson = serialize('geojson',PublicHousing.objects.get(pk=id))
        JsonResponse(json.loads(parcelJson))

def landmarks(request):
    landmarksJson = serialize('geojson',Landmarks.objects.all(), geometry_field='wkb_geometry',fields=('ogc_fid','st_louis_field ',))
    if landmarksJson: 
        result = json.loads(landmarksJson)
        return  JsonResponse(result) 
    else:
        return Http404

def landmarks_byId(id):
    parcelJson = serialize('geojson',Landmarks.objects.get(pk=id))
    JsonResponse(json.loads(parcelJson))



