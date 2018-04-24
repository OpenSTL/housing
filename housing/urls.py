from django.conf.urls import include, url
from django.contrib import admin
from housing import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lra/$', views.lra),
    url(r'^google/$', views.google_forward ) ,
    url(r'^zillow/$', include(admin.site.urls)),
    url('r^lra/byId/(?P<id>d+)/$',views.lra)
]
