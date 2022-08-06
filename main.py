from avas import *

# Init the api
server = avas()

print(" -- AVAS -- ")
print("status: ",server.online)
print("players: ",server.playerCount)
print("clientip: ",server.get_ip())

# Server events
#Wrap the server on_player_join function
@server.event
def on_player_join(quantity):
    print("Player joined")
    print("Player count: ",server.playerCount)
    return

#Wrap the server on_player_leave function
@server.event
def on_player_leave(quantity):
    print("Player left")
    print("Player count: ",server.playerCount)
    return

# start(interval) will start running ping() and polling the events every <interval> seconds
server.start(5)

input()
# Always run stop() otherwise the thread will just keep running
server.stop()