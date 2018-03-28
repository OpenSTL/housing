from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.conf import settings
from .models import Choice, Question
# .
import requests

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        # with POST data. This prevents data from being posted twice if a
def google_forward(lat,lng):
    API_KEY = settings.API_KEYS['google_maps']
    URI = "https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={API_KEY}".format(lat,lng,API_KEY)
    r = requests.get(url = URI)
    data = r.json()

