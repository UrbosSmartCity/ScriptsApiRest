# XML RPC UrbosAPI

from xmlrpc import client

class UrbosAPI():
	def __init__(self,srv,db,user,pwd,model):
		common = client.ServerProxy('%s/xmlrpc/2/common'%(srv))
		self.api = client.ServerProxy('%s/xmlrpc/2/object'%(srv))
		self.user_id = common.authenticate(db,user,pwd,{})
		self.pwd = pwd
		self.db = db
		self.model = model

	def execute(self,method,arg_list,kwar_dict=None):
		return self.api.execute_kw(self.db, self.user_id, self.pwd, self.model, method, arg_list, kwar_dict or{})

	def search_read(self,text=None):
		domain = [('name','ilike',text)] if text else []
		fields = ['id','name']
		return self.execute('search_read',[domain,fields])

	def create(self, measures):
		return self.execute('create', [measures])

	def write(self, title, id):
		vals = {'name': title}
		return self.execute('write',[[id],vals])

	def unlink(self,id):
		return self.execute('unlink', [[id]])


if __name__ == '__main__':
	from pprint import pprint

	# Declare host, database, user and password
	srv = 'https://test.openti.cl'
	db = 'testOpenTI'
	user = 'storeUser'
	pwd = 'password'

	####################################
	#			AIR QUALITY			   #
	####################################

	# Initialize UrbosAPI for Air Quality
	airQualityAPI = UrbosAPI(srv, db, user, pwd, 'air_quality')

	if airQualityAPI.user_id:
		airQualityAPI.create([{
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
		}
		])

		# Print Air Quality records records
		pprint(airQualityAPI.search_read())
		del airQualityAPI

	####################################
	#			CONGESTION			   #
	####################################

	# Initialize UrbosAPI for Congestion
	congestionAPI = UrbosAPI(srv, db, user, pwd, 'congestion')

	if congestionAPI.user_id:
		# Store Congestion measures
		congestionAPI.create([{
			'channelWidth': '2',
			'numberVehicles': '15',
			'vehiclesVelocity': '40',
			'point': '{"type": "LineString", "coordinates": [[-8132918.94,-4413894.45],[-8131709.063961,-4413189.762987]]}'
		},
		{
			'channelWidth': '4',
			'numberVehicles': '15',
			'vehiclesVelocity': '40',
			'line': '{"type": "LineString", "coordinates": [[-8132918.94,-4413894.45],[-8131709.063961,-4413189.762987]]}'
		}])

		# Print Air Quality records records
		pprint(congestionAPI.search_read())
		del congestionAPI
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
		del temperatureAPI
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
		del windSpeedAPI
