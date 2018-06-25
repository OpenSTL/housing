from django.shortcuts import render
from django.contrib.gis.geos import Polygon
from django.core.serializers import serialize 
from django.http import HttpResponseRedirect, HttpResponse , JsonResponse, Http404
from django.urls import reverse
from models import Lra
import json
import requests
#import json

def google_forward(request):
    lat,lng = request.GET['lat'],request.GET['lng']
    API_KEY = settings.API_KEYS['google_maps']
    URI = "https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={API_KEY}".format(lat,lng,API_KEY)
    r = requests.get(url = URI)
    return JsonResponse(r.json())

def lra(request):
    lraJson = serialize('geojson',Lra.objects.all(), geometry_field='wkb_geometry',fields=('id','handle',))
    if lraJson: 
        result = json.loads(lraJson)
        return  JsonResponse(result) 
    else:
        return Http404

def lra_byId(id):
    parcelJson = serialize('geojson',Lra.objects.get(pk=id))
    JsonResponse(json.loads(parcelJson))

def getInfo(request,property_id):
    import zillow 
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
