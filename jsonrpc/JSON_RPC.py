# JSON RPC UrbosAPI

import json
import random
import requests

class UrbosAPI():
	def __init__(self,srv,db,user,pwd,model):
		self.db = db
		self.password = pwd
		self.url = "%s/jsonrpc" % srv
		self.headers = {"Content-Type": "application/json"}
		payload = self.get_json_payload("common", "login", db, user, pwd)
		response = requests.post(self.url, data=payload, headers=self.headers)
		self.user_id = response.json()['result']
		self.model = model

	def get_json_payload(self, service, method, *args):
		return json.dumps({
			"jsonrpc": "2.0",
			"method": 'call',
			"params": {
			"service": service,
			"method": method,
			"args": args
			},
			"id": random.randint(0, 100000000),
		})
	def search_read(self,text=None):
		search_domain = [('point','ilike',text)] if text else []
		# fields = ['id', 'pM10', 'pM2_5', 'sO2', 'cO', 'nO2', 'o3', 'point']
		payload = self.get_json_payload("object","execute_kw",self.db, self.user_id, self.password, self.model, 'search', [search_domain], {'limit':20})
		response = requests.post(self.url, data=payload, headers=self.headers)
		return response.json()['result']

	def create(self, measures):
		payload = self.get_json_payload("object", "execute_kw", self.db, self.user_id, self.password, self.model, 'create',[measures])
		response = requests.post(self.url, data=payload, headers=self.headers)
		return response.json()['result']


if __name__ == '__main__':
	from pprint import pprint

	# Declare host, database, user and password
	srv = 'https://test.openti.cl'
	db = 'testOpenTI'
	user = 'storeUser'
	pwd = 'pass'

	####################################
	#			AIR QUALITY			   #
	####################################

	# Initialize UrbosAPI for Air Quality
	airQualityAPI = UrbosAPI(srv, db, user, pwd, 'air_quality')

	if airQualityAPI.user_id:
		airQualityMeasures = [{
			'pM10': '3',
			'pM2_5': '2',
			'sO2': '5',
			'cO': '4',
			'nO2': '7',
			'o3': '5',
			'point':'{"type": "Point", "coordinates": [-8132918.94,-4413894.45]}'
		},
		{
			'pM10': '3',
			'pM2_5': '2',
			'sO2': '5',
			'cO': '4',
			'nO2': '7',
			'o3': '5',
			'point':'{"type": "Point", "coordinates": [-8132918.94,-4413894.45]}'
		}]

		airQualityAPI.create(airQualityMeasures)

		# Print Air Quality records records
		pprint(airQualityAPI.search_read())

	####################################
	#			CONGESTION			   #
	####################################

	# Initialize UrbosAPI for Congestion
	congestionAPI = UrbosAPI(srv, db, user, pwd, 'congestion')

	if congestionAPI.user_id:
		# Store Congestion measures
		congestionMeasures = [{
			'channelWidth': '2',
			'numberVehicles': '15',
			'vehiclesVelocity': '40',
			'point': '{"type": "LineString", "coordinates": [[-8132918.94,-4413894.45],[-8131709.063961,-4413189.762987]]}'
		},
		{
			'channelWidth': '2',
			'numberVehicles': '15',
			'vehiclesVelocity': '40',
			'line': '{"type": "LineString", "coordinates": [[-8132918.94,-4413894.45],[-8131709.063961,-4413189.762987]]}'
		}]

		congestionAPI.create(congestionMeasures)

		# Print Air Quality records records
		pprint(congestionAPI.search_read())

	####################################
	#			TEMPERATURE			   #
	####################################

	# Initialize UrbosAPI for Congestion
	temperatureAPI = UrbosAPI(srv, db, user, pwd, 'temperature')

	if temperatureAPI.user_id:
		# Store Congestion measures
		temperatureAPI.create([{
			'farenheitDegrees': '5',
			'point':'{"type": "Point", "coordinates": [-8132918.94,-4413894.45]}'
		},
		{
			'farenheitDegrees': '15',
			'point':'{"type": "Point", "coordinates": [-8132918.94,-4413894.45]}'
		}])

		# Print Air Quality records records
		pprint(temperatureAPI.search_read())

	####################################
	#			WIND SPEED			   #
	####################################
	# Initialize UrbosAPI for Congestion
	windSpeedAPI = UrbosAPI(srv, db, user, pwd, 'wind_speed')

	if windSpeedAPI.user_id:
		# Store Congestion measures
		windSpeedAPI.create([{
			'speed': '5',
			'point':'{"type": "Point", "coordinates": [-8132918.94,-4413894.45]}'
		},
		{
			'speed': '15',
			'point':'{"type": "Point", "coordinates": [-8132918.94,-4413894.45]}'
		}])

		# Print Air Quality records records
		pprint(windSpeedAPI.search_read())
