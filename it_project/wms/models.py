from django.db import models
from django.utils import timezone
import math
from twilio.rest import Client




class Plant(models.Model):
	plantID = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	soilMoisture = models.FloatField(default=70)
	temperature=models.FloatField(default=25)
	humidity = models.FloatField(default=40)

	def alert(self):
		# API KEYS,ACCESS?AUTH TOKEN
		client = Client("AC5af5682d318da3011ea161af1eae6de1", "4c8808f82bd9e91ff55abe079f636559")

		client.messages.create(to="+917893448255",
		                       from_="+18652178717",
		                       body="Water tank is almost empty. Watertank needs to refilled soon!")

class waterTank(models.Model):
	radius = models.FloatField()
	height = models.FloatField()
	tankWaterLevel = models.FloatField(default=0)
	volume = models.FloatField(default=0)
	created_on = models.DateTimeField(auto_now_add=True)
	rain = models.IntegerField(default=0)

	def saveVolume(self):
		self.volume = round( (math.pi * self.radius * self.radius) * float(self.tankWaterLevel) )
