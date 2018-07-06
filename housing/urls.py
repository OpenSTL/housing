from django.conf.urls import include, url
from django.contrib import admin
from housing import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^homer/', views.homer),
    url(r'^landmarks/', views.landmarks),
    url(r'^landmarks/byId/(?P<id>d+)', views.landmarks_byId),
    url(r'^publichousing/', views.publichousing),
    #url(r'^zillow/$', include(admin.site.urls)),
]
