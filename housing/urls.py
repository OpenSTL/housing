from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static  
from django.contrib import admin
from django.http import HttpResponseRedirect
from housing import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^homer/', views.homer),
    url(r'^landmarks/', views.landmarks),
    url(r'^landmarks/byId/(?P<id>d+)', views.landmarks_byId),
    url(r'^publichousing/', views.publichousing),
    url(r'^$',lambda r : HttpResponseRedirect('/index.html')  )
    #url(r'^zillow/$', include(admin.site.urls)),
] + static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
