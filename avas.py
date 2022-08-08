import requests
import json
import threading
import time

#Scratchdragon made this bullshit code

class api_session:
	ip = ""
	authenticated = False
	authAttempts = 0
	requestCount = 0
	requestResetTime = ""
	def __init__(self,ip,auth,auth_attempts,requests,restime):
		self.ip = ip
		self.authenticated = auth
		self.authAttempts = auth_attempts
		self.requestCount = requests
		self.requestResetTime = restime
	
class avas:
	api = requests.get('https://api.avas.cc/ping')
	online = False
	playerCount = 0
	tps = 0
	messagesBlocked = 0
	messagesSend = 0
	
	_playercount_old = 0
	_interval = 10
	__thread=0
	__stop=False

	def api_get(self,item):
		self.api = requests.get('https://api.avas.cc/'+item)

	def api_element(self,elem):
		try:
			return json.loads(self.api.text)[elem]
		except:
			return 0
	
	def ping(self):
		#ping will refresh all of the data
		self.get_online()
		self.get_stats()
		return self.online

	def get_online(self):
		self.api_get("ping")
		self.online = bool(self.api_element("success"))
		return self.online
		
	def get_stats(self):
		self.api_get("stats")
		#Player count
		self.playerCount = self.api_element("playerCount")
		if(self._playercount_old != self.playerCount):
			if(self._playercount_old > self.playerCount):
				self.on_player_leave(self._playercount_old-self.playerCount)
			else:
				self.on_player_join(self.playerCount-self._playercount_old)
			self._playercount_old=self.playerCount
		#TPS
		self.tps = self.api_element("tps")
		#Message counts
		self.messageSent = self.api_element("messagesSent24h")
		self.messagesBlocked = self.api_element("messagesBlocked24h")
		return self.tps

	def get_session(self):
		self.api_get("myip")
		ip = self.api.text
		self.api_get("session")
		
		return api_session(ip,
			self.api_element("authenticated"),
			self.api_element("failedAuthRequests"),
			self.api_element("requestCount"),
			self.api_element("requestResetTime")
		)

	def _loop(self):
		while(not self.__stop) :
			self.ping()
			time.sleep(self._interval)

	def start(self,interval):
		self._interval = interval
		self.__thread.start()

	def stop(self):
		self.__stop=True

	def __init__(self):
		self.__thread = threading.Thread(name='background', target=self._loop, args=[])
		self.ping()
		
	#Events
	def on_player_join(self,quantity):
		pass
	def on_player_leave(self,quantity):
		pass

	# Event decorator
	def event(self,func):
		setattr(self, func.__name__, func)
		return func