from django.conf import settings
from django.shortcuts import render
from django.contrib.gis.geos import Polygon
from django.core.serializers import serialize 
from django.http import HttpResponseRedirect, HttpResponse , JsonResponse, Http404
from django.urls import reverse
#from models import BuildingFootprints,Landmarks,PublicHousing,FinalVacant
from models import Landmarks,PublicHousing,FinalVacant
import json



def index(request):
    return render(request, 'index.html' )
    
def vacant_parcels_byId(id):
    finalVacant = serialize('geojson',FinalVacant.objects.get(pk=id), geometry_field='geom',fields=('siteaddr','resunits','acres','zoning','parcelid','zip'))
    JsonResponse(json.loads(VacantParcelJson))

def homer(request):
    GET = request.GET
    plotChoice = GET['plotChoice'] 
    userQuery = FinalVacant.objects.filter(acres__gt=GET['minAcres'],nbrhd=GET['nbrhd'])
    if plotChoice == 'vacant_building':
        userQuery = userQuery.filter( price__vacant_building__gt=GET['minprice'],price__vacant_building__lt=GET['maxprice'])
        # sl = sidelot 
    elif plotChoice == 'new_construction':
        userQuery = userQuery.filter( price__new_construction__gt=GET['minprice'],  price__new_construction__lt=GET['maxprice'])
        # nc = new contsruction 
    elif plotChoice == 'vacant_lot':
       userQuery = userQuery.filter( price__vacant_lot__gt=GET['minprice'], price__vacant_lot__lt=GET['maxprice'])
        # vl = vacant lot 
    else: 
        # vb = vacant buliding 
        userQuery = userQuery.filter( price__vacant_building__gt=GET['minprice'],  price__vacant_building__lt=GET['maxprice'])
    print userQuery
    resultJson = serialize('geojson',userQuery.order_by( outcomes), geometry_field='geom',fields=('siteaddr', 'tifdist','acres' ))
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



