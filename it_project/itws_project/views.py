from django.shortcuts import redirect,render,get_object_or_404
from django.http import HttpResponse
from xml.dom import minidom
import urllib2, urllib, json
import unicodedata

def dashboard(request):
	''' to get weather forecasts for the next 9 days using yahoo weather api'''
	baseurl = "https://query.yahooapis.com/v1/public/yql?"
	# item.forecast is variable...can be replaced with wind_speed or so -------- woeid is the id for city and u= c means that it is metric system i.e., CElcius
	yql_query = "select item.forecast from weather.forecast where woeid=2295279 AND u='c'"
	#making the url from the dictionry created ,for sending ...urlopen has and made to json format 
	yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
	#here it reads it and stores the final thing as a object of JSON
	result = urllib2.urlopen(yql_url).read()
	#it is dictionary...the JSON object  is made into dictionary 
	data = json.loads(result)
    # we select the required item that is the correspoding dictionary of query and results
	forecast = data['query']['results']

	#creating a list (of lists) for sending the weather forecasts to the webpage
	forecasts = []
	for i in range(9):
		L = [1,2,3,4]
		#u'------it shows the unicode encoding
		a = forecast[u'channel'][i][u'item'][u'forecast'][u'date']
		b = forecast[u'channel'][i][u'item'][u'forecast'][u'low']
		c = forecast[u'channel'][i][u'item'][u'forecast'][u'high']
		# the text corresponds to codtion like cloudy or sunny etc
		d = forecast[u'channel'][i][u'item'][u'forecast'][u'text']
		# it can also be replaced with NFC,NFD...these are just methods of normailisation
		L[0] = unicodedata.normalize('NFKD', a).encode('ascii','ignore')
		L[1] = unicodedata.normalize('NFKD', b).encode('ascii','ignore')
		L[2] = unicodedata.normalize('NFKD', c).encode('ascii','ignore')
		L[3] = unicodedata.normalize('NFKD', d).encode('ascii','ignore')
		forecasts.append(L)

	return render(request, 'wms/Dashboard_mist/pages/base.html', { 'forecasts' : forecasts })
