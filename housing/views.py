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
    
def vacant_parcels_byId(handle):
    finalVacant = serialize('geojson',FinalVacant.objects.get(handle=handle), geometry_field='geom',fields=('siteaddr','resunits','acres','zoning','parcelid','zip'))
    JsonResponse(json.loads(VacantParcelJson))

def homer(request):
    GET = request.GET
    plotChoice = GET['plotChoice'] 
    if GET['nbrhd'] == 'any':
        userQuery = FinalVacant.objects.all()
        testQuery= userQuery.all()[:5]
    else:
        userQuery = FinalVacant.objects.all()
        testQuery= userQuery.filter(nbrhd = GET['nbrhd'])
    #if plotChoice == 'vb':
        #userQuery = userQuery.filter( price__bldg_price__gt=GET['minprice'],price__bldg_price__lt=GET['maxprice'])
        # vb = vacant buliding 
    #elif plotChoice == 'nc':
        #userQuery = userQuery.filter( price__new_construction_price__gt=GET['minprice'],price__new_construction_price__lt=GET['maxprice'])
        # nc = new contsruction 
    #elif plotChoice == 'sl':
       #userQuery = userQuery.filter( price__side_lot_price__gt=GET['minprice'], price__side_lot_price__lt=GET['maxprice'])
        # vl = vacant lot 
    #else: 
        # sl = sidelot 
        #userQuery = userQuery.filter( price__vacant_building_price__gt=GET['minprice'],  price__vacant_building_price__lt=GET['maxprice'])
    #print len(userQuery)
    resultJson = serialize('geojson',testQuery, geometry_field='geom',fields=('siteaddr','resunits','acres','zoning','parcelid','zip'))
    if  resultJson:
        return JsonResponse(json.loads(resultJson))
    else:
        return Http404 

def publichousing(request):
    publichousingJson = serialize('geojson',PublicHousing.objects.all(), geometry_field='wkb_geometry',fields=('id','handle'))
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



