from django.conf.urls import include, url
from django.contrib import admin
from housing import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^landmarks/', views.landmarks),
    url(r'^landmarks/byId/(?P<id>d+)', views.landmarks_byId),
    url(r'^publichousing/', views.publichousing),
    url(r'^vacant_parcels/', views.vacant_parcels),
    url(r'^vacant_parcels/byId/(?P<id>d+)', views.vacant_parcels_byId),
    url(r'^lra/', views.lra),
    url('r^lra/byId/(?P<id>d+)/$',views.lra),
    #url(r'^zillow/$', include(admin.site.urls)),
]
