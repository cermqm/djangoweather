from django.shortcuts import render

def home(request):
	import json
	import requests

	#api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=64118&distance=25&API_KEY=02230735-351B-41BE-A658-6F615745AC69")
	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=77010&distance=100&API_KEY=02230735-351B-41BE-A658-6F615745AC69")

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."

	if api[0]['Category']['Name'] == "Good":
		#category_description = "{{api[0]['ParameterName']}} AQI is 0-50 - Air Quality is Satisfactory, adn air polution pose little or no risk."
		category_description = "O3 AQI is 0-50 - Air Quality is Satisfactory, adn air polution pose little or no risk."
		category_color = "good"
	elif api[0]['Category']['Name'] == "Moderate":
		category_description = "O3 AQI is 51-100 - Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
		category_color = "moderate"
	elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
		category_description = "O3 AQI is 101-150 - Members of sensitive groups may experience health effects. The general public is less likely to be affected."
		category_color = "usg"
	elif api[0]['Category']['Name'] == "Unhealthy":
		category_description = "O3 AQI is 151-200 - Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
		category_color = "unhealthy"
	elif api[0]['Category']['Name'] == "Very Unhealthy":
		category_description = "O3 AQI is 201-250 - Health alert: The risk of health effects is increased for everyone."
		category_color = "veryunhealhy"
	elif api[0]['Category']['Name'] == "Hazardous":
		category_description = "O3 AQI is 251-300 - Health warning of emergency conditions: everyone is more likely to be affected."
		category_color = "hazardous"

	return render(request, 'home.html', {'api': api,
		'category_description': category_description,
		'category_color': category_color})

def about(request):
	return render(request, 'about.html', {})