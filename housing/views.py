from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import zillow
import json

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