from django.shortcuts import render
from django.contrib.gis.geos import Polygon
from django.core.serializers import serialize 
from django.http import HttpResponseRedirect, HttpResponse , JsonResponse
from django.urls import reverse
import zillow
import requests
import json

def google_forward(request):
    lat,lng = request.GET['lat'],request.GET['lng']
    API_KEY = settings.API_KEYS['google_maps']
    URI = "https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={API_KEY}".format(lat,lng,API_KEY)
    r = requests.get(url = URI)
    return JsonResponse(r.json())

def lra(request):
    #top=49.5138 left=10.9351 bottom=49.3866 right=11.201
    xmin = request.GET['sw']
    ymin = request.GET['ne']
    xmax = request.GET['se']
    ymax = request.GET['nw']
    bbox = (xmin, ymin, xmax, ymax)
    geom = Polygon.from_bbox(bbox)
    lraJson = serialize('geojson',lra.objects.filter(poly__contained=geom), geometry_field='geom', fields=('fulladdress','cost'))
    JsonResponse(lraJson)

def getInfo(request, property_id):
    with open("./bin/config/zillow_key.conf", 'r') as f:
        key = f.readline().replace("\n", "")

    api = zillow.ValuationApi()

    property = get_object_or_404(Property, pk=property_id)
    selected_property = property.property_list.get(pk=request.POST['address'])

    address = selected_property + ', St. Louis, MO'

    data = api.GetDeepSearchResults(key, address, postal_code)

    return HttpResponse(json.dumps({'foo': 'bar'}), mimetype='application/json')

    #return HttpResponseRedirect(reverse('property', args=(property.id,)))




"""<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"></script>
<script type="text/javascript">
 $.get('/ajax/', function(data) {
   alert(data['foo']);
 });
</script>"""
