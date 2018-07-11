from django.conf import settings
from django.shortcuts import render
from django.contrib.gis.geos import Polygon
from django.core.serializers import serialize 
from django.http import HttpResponseRedirect, HttpResponse , JsonResponse, Http404
from django.urls import reverse
from models import Landmarks,PublicHousing,FinalVacant
import json



def index(request):
    return render(request, 'index.html' )
    
def vacant_parcels_byId(handle):
    finalVacant = serialize('geojson',FinalVacant.objects.get(handle=handle), geometry_field='geom',fields=('siteaddr','resunits','acres','zoning','parcelid','zip'))
    return JsonResponse(json.loads(finalVacant))

def vacant_test(request):
    finalVacant = serialize('geojson',FinalVacant.objects.filter(nbrhd=1)[:10], geometry_field='geom',fields=('siteaddr','resunits','acres','zoning','parcelid','zip'))
    return JsonResponse(json.loads(finalVacant))

def homer(request):
    GET = request.GET
    plotChoice = GET['plotChoice'] 
    userQuery = FinalVacant.objects.all()
    if GET['nbrhd'] != '0':
        userQuery = userQuery.filter(nbrhd =int( GET['nbrhd']))
    if 'maxprice' in GET or 'minprice' in GET:
        if plotChoice == 'vb':
        # vb = vacant buliding 
            if 'maxprice' in GET: 
                userQuery = userQuery.filter(price__bldg_price__lt=GET['maxprice'])
            if 'minprice' in GET:
                userQuery = userQuery.filter(price__bldg_price__gt=GET['minprice'])
        elif plotChoice == 'nc':
            # nc = new contsruction 
            if 'maxprice' in GET: 
                userQuery = userQuery.filter( price__new_construction_price__gt=GET['minprice'])
            if 'minprice' in GET:
                userQuery = userQuery.filter( price__new_construction_price__lt=GET['maxprice'])
        elif plotChoice == 'sl':
            # sl = sidelot 
            if 'maxprice' in GET: 
               userQuery = userQuery.filter( price__side_lot_price__gt=GET['minprice'])
            if 'minprice' in GET:
               userQuery = userQuery.filter(price__side_lot_price__lt=GET['maxprice'])
    print userQuery.query
    resultJson = serialize('geojson',userQuery, geometry_field='geom',fields=('siteaddr','resunits','acres','zoning','parcelid','zip','vb','sl','nc','vl'))
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



