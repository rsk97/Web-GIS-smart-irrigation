from django.shortcuts import redirect,render,get_object_or_404
from .models import Plant,waterTank
from django.http import HttpResponse
from django.utils import timezone
import json
# Create your views here.

def plant_list(request):
	'''to get the list and display all the plants'''
	d=[]
	A = Plant.objects.all()
	for i in A:
		if i.plantID not in d:
			d.append(i.plantID)

	return render(request, 'wms/Dashboard_mist/pages/plant_list.html', {'p1':d[0], 'p2':d[1], 'length' : len(d), 'p':d })

def plant_detail(request,pID):
	'''To display the details of a specified plant'''
	x=Plant.objects.filter(plantID=pID).order_by('-created_on')

	arr = []
	current = timezone.now()

	for p in x:
		delta = current - p.created_on
		if delta.seconds >= 3600:
			current = p.created_on
			arr.append(json.dumps({'temperature': p.temperature, 'humidity': p.humidity, 'soilMoisture' : p.soilMoisture}))

	return render(request,'wms/Dashboard_mist/pages/plant_details.html',{'plantsjson': arr, 'plants': x,'latest':x[0], 'levelx':waterTank.objects.order_by("-created_on")[0].tankWaterLevel})

def grab(request):
	'''This function recieves the details of the plants sent by the raspberry pi and it creates a new plant object using the recieved data'''
	temp = request.GET['t']
	plantID=request.GET['plantID']
	soilMoisture = request.GET['s']
	humidity = request.GET['h']
	Plant.objects.create(plantID=plantID,temperature = temp,soilMoisture = soilMoisture,humidity = humidity)

	return redirect("plant_detail",pID=plantID)


def showTank(request):
	'''To display the details of the water tank'''
    x = waterTank.objects.order_by("-created_on")

    arr = []
    current = timezone.now()

    for p in x:
        delta = current - p.created_on
        if delta.seconds >= 3600:
            current = p.created_on
            level = p.tankWaterLevel
        arr.append(json.dumps({'level': level}))


    t = waterTank.objects.order_by("-created_on")[0]
	level = waterTank.objects.order_by("-created_on")[0].tankWaterLevel
	if level < 10:
		t.alert()
	return render(request,"wms/Dashboard_mist/pages/water_tank_details.html",{'plantsjson': arr, 'tank':waterTank.objects.order_by("-created_on")[0],'levelx':level})


def waterLevel(request):
	'''The water tank details sent by raspberry pi is recieved by this function and the data is stored as a new tank object'''
	level = request.GET['level']
	rain = request.GET['rain']
	t = waterTank.objects.all()[0]

	waterTank.objects.create(tankWaterLevel=level,radius=t.radius,height=t.height,rain = rain)
	t = waterTank.objects.order_by("-created_on")[0]
	t.saveVolume()
	t.save()

	x = waterTank.objects.order_by("-created_on")

	arr = []
	current = timezone.now()

	for p in x:
		delta = current - p.created_on
		if delta.seconds >= 3600:
			current = p.created_on

			arr.append(json.dumps({'level': level}))

	t = waterTank.objects.order_by("-created_on")[0]
	return render(request,"wms/Dashboard_mist/pages/water_tank_details.html",{'plantsjson': arr, 'tank':waterTank.objects.order_by("-created_on")[0],'levelx':level})


def dimensions(request):
	'''This sets and saves the dimensions of the tank.While setting up the tank we first have to give it's dimensions using this function'''
    radius = request.GET['r']
    height = request.GET['h']

    if waterTank.objects.all().count() == 0:
        waterTank.objects.create(radius=radius,height=height)
    else:
        x = waterTank.objects.all()[0]
        x.radius = radius
        x.height = height
        x.save()

    x = waterTank.objects.order_by("-created_on")

    arr = []
    current = timezone.now()

    for p in x:
        delta = current - p.created_on
        if delta.seconds >= 3600:
            current = p.created_on
        arr.append(json.dumps({'level': z}))


    t = waterTank.objects.order_by("-created_on")[0]
    return render(request,"wms/Dashboard_mist/pages/water_tank_details.html",{'plantsjson': arr, 'tank':waterTank.objects.order_by("-created_on")[0],'levelx':t.height-t.tankWaterLevel})



def showMap(request):
	''' This function shows the location of plants on map and displays the object values on the map'''
	plant1 = Plant.objects.filter(plantID=1).order_by('-created_on')[0]
	plant2 = Plant.objects.filter(plantID=2).order_by('-created_on')[0]
	t = waterTank.objects.order_by("-created_on")[0]
	rain = t.rain

	return render(request,"wms/Dashboard_mist/pages/maps.html",{'plant1' : plant1,'plant2' : plant2,'tank' : t.tankWaterLevel , 'rain' : rain})
