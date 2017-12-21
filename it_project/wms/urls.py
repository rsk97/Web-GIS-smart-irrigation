from django.conf.urls import url
from . import views

urlpatterns = [
    #to see the list of plants
    url(r'^$', views.plant_list, name='plants_list'),
    #to get the details of a specific plant
    url(r'^(?P<pID>\d+)/$', views.plant_detail, name='plant_detail'),
    #to get the data of plant and temperature
    url(r'^getdata/$',views.grab,name="grab_data"),
    #to set the dimensions of the tank
    url(r'^getdimensions/$',views.dimensions,name="enter_dimensions"),
    #to get waterlevel for the tank
    url(r'^getWaterLevel/$',views.waterLevel,name="waterLevel"),
    #to get the map with the details of the objects
    url(r'^showLocation/$',views.showMap,name="map"),
    #to show the tank details
    url(r'^showTank/$',views.showTank,name="tankDetails"),
]
