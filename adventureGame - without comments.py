#Secret Agent Adventure Game
#by Alex Hadwen-Bennett

rooms={"Street":"outside the HQ",
       "Lobby":"the lobby of the HQ",
       "Lift":"the main lift",
       "1st Floor":"the first floor of the HQ"}

exits={"Street":{"east":["Lobby"]},
       "Lobby":{"west":["Street"],"north":["Lift"]},
       "Lift":{"south":["Lobby"],"up":["1st Floor","KeyCard"]},
       "1st Floor":{"north":["Lift"]}}

objects={"Street":[],
       "Lobby":["WelcomeMat","KeyCard"],
       "Lift":[],
       "1st Floor":[]}

hidden={"WelcomeMat":"KeyCard"}

inventory=[]

def roomDetails(room):
    print("\nCurrent Location:",room,"-",rooms[room])
    if len(objects[room]) > 0:
        print("Objects:")
        for object in objects[room]:
            if object not in hidden.values():
                print(object)

def go(direction,room):
    possible=False
    if direction in exits[room]:
        if len(exits[room][direction])==1:     
            possible=True
        elif len(exits[room][direction])>1:
            if exits[room][direction][1] in inventory:
                possible=True
    if possible==True:
        room=exits[room][direction][0]
        roomDetails(room)
    else:
        print("It's not currently possible to move in that direction")
    return room

def move(object,room):
    if object in hidden and object in objects[room]:
        print("You have moved",object,"and revealed:",hidden[object])
        del hidden[object]
    else:
        print("It isn't possible to move this object")

def collect(object,room):
    if object in objects[room]:
        inventory.append(object)
        print(object,"has been added to your inventory.")
    else:
        print("It isn't possible to add this object to your inventory.")

print("You are a secret agent and you need to steal the plans for the enemy's new weapon from their HQ.")
print("\nThe following commands are available to you:\nGO - move north, south, east, west, up or down (e.g. go north)\nMOVE - move an object (e.g. move chair)\nCOLLECT - collect an object (e.g. collect key)")

currentRoom="Street"
roomDetails(currentRoom)

while True:
    command=input(": ")
    command=command.split()
    if command[0].lower()=="go":
        currentRoom=go(command[1].lower(),currentRoom)
    elif command[0].lower()=="move":
        move(command[1],currentRoom)
    elif command[0].lower()=="collect":
        collect(command[1],currentRoom)
    else:
        print("I'm sorry I didn't understand that command.")
    
