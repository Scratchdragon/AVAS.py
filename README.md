# AVAS.py
A python module for the AVAS minecraft server api

### Usage
To use the api just add the avas.py file to your project and import it with "from avas import *" or "from avas import avas".
Theres a very basic example for how to use the module in the main.py file

### Variables
The variables are updated whenever ping() is called __or__ when the events are updated by avas.start()
- online : returns true/false depending on if the server is up
- playerCount : returns the number of currently logged in players
- tps : returns the servers tps
- messagesSent : returns the amount of messages sent in 24 hours
- messagesBlocked : returns the amount of messages blocked in 24 hours

### Functions
- ping() : returns server online, refreshes all variables
- get_online() : returns server online, refreshes "online" variable
- get_stats() : returns tps, refreshes tps, playerCount, messagesSent, messagesBlocked
- get_session() : returns the session data of the client in the form of a "api_session" class

### Classes

**api_session**<br>
This class is returned by get_session() and consists of five variables:
- ip : the clients ip
- authenticated : if the session is authenticated
- authAttempts : how many failed auth attempts have occured
- requestCount : how many requests have been sent in the current session
- requestResetTime : the time since last request reset

### Events
- on_player_join(quantity) : runs whenever a player joins
- on_player_leave(quantity) : runs whenever a player leaves

To use events you simply need to wrap them using @server.event. For example
```
server = avas()

@server.event
def on_player_join(quantity) :
    print("Player joined")

server.start(5) #start polling events every 5 seconds to avoid throttling the api server
```
The above code will print "Player Joined" whenever a player joins<br>
Polling events will also run ping() each time, updating the variables dependant on it<br>
**Always run server.stop() at the end of you script** since otherwise it will be quite hard to stop the project


I am currently working on getting this package ready for PIP but my python experience is pretty limmited so this may take some time. If you wanna help out with doing packaging then just let me know
