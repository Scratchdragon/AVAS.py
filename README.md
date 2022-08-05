# AVAS.py
A python module for the AVAS minecraft server api

### Usage
To use the api just add the avas.py file to your project and import it with "from avas import *" or "from avas import avas".

### Variables
The variables are updated whenever ping() is called
- online : returns true/false depending on if the server is up
- playerCount : returns the number of currently logged in players

### Functions
- ping() : returns server online, refreshes all variables
- get_online() : returns server online, refreshes "online" variable
- get_playercount() : returns playercount, refreshes "playerCount" variable