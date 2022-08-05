import requests
import json

#Scratchdragon made this bullshit code

class avas:
	api = requests.get('https://api.avas.cc/ping')
	online = False
	playerCount = 0
	
	def api_get(self,item):
		# just so im not writing request.get too much
		self.api = requests.get('https://api.avas.cc/'+item)
	def api_element(self,elem):
		return json.loads(self.api.text)[elem]
	
	def ping(self):
		#ping will refresh all of the data
		self.api_get("ping")
		self.online = self.api_element("success")
		self.get_playercount()
		return self.online

	def get_online(self):
		#pretty much ping() but without get_playercount
		self.api_get("ping")
		self.online = self.api_element("success")
		return self.online
		
	def get_playercount(self):
		self.api_get("stats")
		self.players = self.api_element("playerCount")
		return self.players

	def __init__(self):
		self.ping()

avas = avas()
print(avas.playerCount)