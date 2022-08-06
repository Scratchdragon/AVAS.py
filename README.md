# AVAS.py
A python module for the AVAS minecraft server api

### Usage
To use the api just add the avas.py file to your project and import it with "from avas import *" or "from avas import avas".
Theres a very basic example for how to use the module in the main.py file

### Variables
The variables are updated whenever ping() is called
- online : returns true/false depending on if the server is up
- playerCount : returns the number of currently logged in players

### Functions
- ping() : returns server online, refreshes all variables
- get_online() : returns server online, refreshes "online" variable
- get_playercount() : returns playercount, refreshes "playerCount" variable
- get_ip() : gets the ip of the api client

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
Polling events will also run ping() each time, updating the variables dependant on it


I am currently working on getting this package ready for PIP but my python experience is pretty limmited so this may take some time. If you wanna help out with doing packaging then just let me know