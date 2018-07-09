from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.views.static import serve
from housing import views

urlpatterns = [
    url(r'^$', views.index),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^homer/', views.homer),
    url(r'^landmarks/', views.landmarks),
    url(r'^landmarks/byId/(?P<id>d+)', views.landmarks_byId),
    url(r'^publichousing/', views.publichousing),
    url(r'^static/(?P<path>.*)$',serve, { 'document_root': settings.STATIC_ROOT, 'show_indexes': True})
    #url(r'^zillow/$', include(admin.site.urls)),
] 
