###########################################################################################
# Name: Luke Moore, Wyatt Stephens, Denish Pokhrel
# Date: 9/29/2021
# Description: We have reimplemented our previous Room Adventure Program with many new additions,
# such as new rooms and floors, exits, items and descriptions, and grabbables. In addition, we have added a player score
# variable, which increases with each grabbable that the user takes. We have also added new ways which the player can die,
# such as jumping off the balcony.
###########################################################################################
from tkinter import *

# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Room:
    # the constructor
    def __init__(self, name, image):
        # rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
        # and grabbables (things that can be taken into inventory)
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate dictionary
        self._exits[exit] = room

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate dictionary
        self._items[item] = desc

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)

    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)

        # next, the items in the room
        s += "You see: "
        for item in self.items.keys():
            s += item + " "
        s += "\n"

        # next, grabbables in the room
        s += "You can take: "
        for grabbable in self.grabbables:
            s += grabbable + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits.keys():
            s += exit + " "

        return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):


    # the constructor
    def __init__(self, parent):
        # call the constructor in the superclass
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
                r1 = Room("Room 1","room1.gif")
                r2 = Room("Room 2","room2.gif")
                r3 = Room("Room 3","room3.gif")
                r4 = Room("Room 4","room4.gif")
                r5 = Room("Kitchen","room5.gif")
                r6 = Room("Room 6","room6.gif")
                basement=Room("Basement: Once you enter, the doors Get locked","basement.gif")
                bathroom=Room("Bathroom","bathroom.gif")
                attic=Room("Attic","attic.gif")
                r10 = Room("Study", "study.gif")
                r11 = Room("Game Room", "game.gif")
                r12 = Room("Balcony", "balcony.gif")

                # add exits to room 1
                r1.addExit("east",r2)
                r1.addExit("south",r3)
                r1.addExit("west", r5)
                # add grabbables to room 1
                r1.addGrabbable("key")
                # new grabbable
                r1.addGrabbable("treasure_map")
                # add items to room 1
                r1.addItem("chair","It is made of wicker and no one is sitting on it.")
                r1.addItem("table","It is made of oak. A golden key rests on it.")

                # add exits to room 1
                r2.addExit("west",r1)
                r2.addExit("south",r4)
                r2.addExit("east",r6)
                r2.addExit("upstairs", r10)
                # add items to room 2
                r2.addItem("rug","It is nice and Indian, and needs to be vacuumed.")
                r2.addItem("fireplace","It is full of ashes.")
                r2.addItem("table", "has a pack of batteries")
                # new grabbable
                r2.addGrabbable("broom")
                r2.addGrabbable("batteries")

                # add exist to room 3
                r3.addExit("north",r1)
                r3.addExit("east",r4)
                r3.addExit("west", r5)
                r3.addExit("south", bathroom)
                # add grabbable
                r3.addGrabbable("book")
                # new grabbable
                r3.addGrabbable("pen")
                r3.addItem("statue","There is nothing special about it.")
                r3.addItem("desk","The statue is resting on it. So is a book.")

                # add exits to room 4
                r4.addExit("north",r2)
                r4.addExit("west",r3)
                r4.addExit("east",r6)
                r4.addExit("south",None) # Death!
                # new grabbable
                r4.addGrabbable("empty_mug")
                r4.addGrabbable("6-pack")
                # add item to room 4
                r4.addItem("brew_rig","Gourd is brewing some kind of oatmeal stout on the brew rig. A 6-pack is beside it.")

                # new rooms, each with new items, exits, and grabbables
                # add exits to room 5
                r5.addExit("north", r1)
                r5.addExit("south", r3)
                # add items to room 5
                r5.addItem("fridge","energy drinks are in it")
                r5.addItem("sink", "contains dishes")
                r5.addItem("cabinet","sharp knife in it")
                # add grabbables to room 5
                r5.addGrabbable("knife")
                r5.addGrabbable("energy_drinks")

                # add exits to room 6
                r6.addExit("downstairs",basement)
                r6.addExit("north",r2)
                r6.addExit("south",r4)
                # add items to room 6
                r6.addItem("stairs", "leads to basement")
                r6.addItem("rocking_chair", "has a lighter on top of it")
                r6.addItem("tv" , "weather channel is on")
                r6.addItem("safe" , "could have money. Type try safe to attempt to unlock it")
                # add grabbable to room 6
                r6.addGrabbable("lighter")

                # add exit to basement
                basement.addExit("upstairs", None)
                # add items to room basement
                basement.addItem("Pool Table", "Pool table has missing numbers")
                basement.addItem("Cabinet"," full of spider webs")

                # add exit to attic
                attic.addExit("downstairs", r11)
                # add items to attic
                attic.addItem("boxes", "flashlight in it")
                attic.addItem("thrash_bags","christmas lights")
                attic.addItem("drawer","has duct_tape")
                # add grabbables to attic
                attic.addGrabbable("flashlight")
                attic.addGrabbable("duck tape")

                # add exit to bathroom
                bathroom.addExit("north", r3)
                # add items to bathroom
                bathroom.addItem("drawer", "bunk of junk")
                bathroom.addItem("cabinet", "has first_aid_kit")
                # add grabbable to bathroom
                bathroom.addGrabbable("first_aid_kit")

                # add exits to room 10
                r10.addExit("downstairs", r2)
                r10.addExit("west", r11)
                # add items to room 10
                r10.addItem("desk", "The desk has papers scattered across it.")
                r10.addItem("bookcase", "It is filled with books from around the world.")

                # add exits to room 11
                r11.addExit("upstairs", attic)
                r11.addExit("north", r12)
                r11.addExit("east", r10)
                # add items to room 11
                r11.addItem("animal heads", "There are a variety of animals from different parts of the world.")

                # add exits to room 12
                r12.addExit("south", r11)
                r12.addExit("down", None)

                # set room 1 as current room at beginning of game
                Game.currentRoom = r1

                # initialize the player's inventory
                Game.inventory = []

                # initialize the player's score, new variable to keep track of points
                Game.score = 0

    # sets up the GUI
    def setupGUI(self):
                #  organize the GUI
                self.pack(fill=BOTH,expand=1)

                # set up the player input bar at the bottom of the GUI
                # the widget is a Tkinter Entry
                # set its background to white and bind the return key to the function process in the class
                # push it to the bottom of the GUI and let it fill horizontally
                # give it focus so the player doesn't have to click on it
                Game.player_input = Entry(self, bg = "white")
                Game.player_input.bind("<Return>",self.process)
                Game.player_input.pack(side=BOTTOM, fill=X)
                Game.player_input.focus()

                # set up the image to the left of the GUI
                # the widget is a Tkinter Label
                # don't let the image control the widget's size
                img = None
                Game.image = Label(self, width=WIDTH // 2, image=img)
                Game.image.pack(side=LEFT, fill=Y)
                Game.image.pack_propagate(False)

                # set up the text to the right of the GUI
                # first, the frame in which the text will be placed
                text_frame = Frame(self, width=WIDTH // 2)
                # the widget is a Tkinter frame
                # disable it by default
                # don't let the widget control the frame's size
                Game.text = Text(text_frame,bg="lightgrey",state=DISABLED)
                Game.text.pack(fill=Y,expand=1)
                text_frame.pack(side=RIGHT,fill=Y)
                text_frame.pack_propagate(False)

    # sets the current room image, img = picture itself, image = photo container
    def setRoomImage(self):
                if (Game.currentRoom == None):
                        Game.img = PhotoImage(file="skull.gif")
                else:
                        Game.img = PhotoImage(file=Game.currentRoom.image)

                # display the image on the left side of the GUI
                Game.image.config(image=Game.img)
                Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
                # enable the text widget, clear it, set it, disable it
                Game.text.config(state=NORMAL)
                Game.text.delete("1.0", END)
                if (Game.currentRoom == None):
                        # if dead, let the player know
                        # updates player score if user dies, and lets the player know
                        # that their score has been updated
                        Game.score = 0
                        Game.text.insert(END, "You are dead. The only thing you can do now is quit. Your score is now 0. \n")
                else:
                        # otherwise, display the appropriate status
                        # new addition - displays user's score
                        Game.text.insert(END, str(Game.currentRoom) +\
                                         "\nYou are carrying: " + str(Game.inventory) +\
                                         "\n\n" + status + "\n" + "Your score is " + str(Game.score))
                        Game.text.config(state=DISABLED)

    # plays the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status
        self.setStatus("")




    # processes the player's input
    def process(self, event):
                # grab the player's input from the input at the bottom of
                # the GUI
                action = Game.player_input.get()
                # set the user's input to lowercase to make it easter to
                # compare the verb and noun to known values
                action = action.lower()
                # set a default response
                response = "I don't understand. Try verb noun. Valid verbs are go, look, and take."

                # exit the game if the player wants to leave (supports quit,
                # exit, and bye)
                if (action == "quit" or action == "exit" or action == "bye" or action == "sionara!"):
                        exit(0)

                # if the player is dead if goes/went south from room 4
                if (Game.currentRoom == None):

                        # clear the player input
                    Game.player_input.delete(0,END)
                    return
                # split the user input into words ( words are separated by
                # spaces) and store the words in a list
                words = action.split()

                # the game only understands two word inputs
                if (len(words) ==2):
                        # isolate the verb and noun
                        verb = words[0]
                        noun = words[1]


                        # the verb is: go
                        if (verb == "go"):
                                # set default response
                                response = "Invalid exit."

                                # check for valid exits in the current room
                                if (noun in Game.currentRoom.exits):
                                        # if one is found, change the current room too
                                        # the one that is associated with the
                                        # specified exit
                                        Game.currentRoom =\
                                                         Game.currentRoom.exits[noun]
                                        # set the response (success)
                                        response = "Room changed."
                        # the verb is look
                        elif (verb == "look"):
                                # set a default response
                                response = "I don't see that item."

                                # check for valid items in tghe current room
                                if (noun in Game.currentRoom.items):
                                        # if one is found, set the response to the
                                        # item's description
                                        response = Game.currentRoom.items[noun]


                        # the verb is: take
                        elif (verb == "take"):
                                # set a default response
                                response = "I don't see that item."

                                # check for valid grabbable items in the current room
                                for grabbable in Game.currentRoom.grabbables:
                                        # a valid grabbable item is found
                                        if (noun == grabbable):
                                                # add the grabbable item to the player's inventory
                                                Game.inventory.append(grabbable)
                                                # increment the player's score
                                                Game.score = Game.score + 15
                                                # remove the grabbable item from the room
                                                Game.currentRoom.delGrabbable(grabbable)
                                                # set the response(success)
                                                response = "Item grabbed."
                                                # no need to check any more grabbable items
                                                break
                                            


                # display the response on the right of the GUI
                # display the room's image on the left of the GUI
                # clear the player's input
                self.setStatus(response)
                self.setRoomImage()
                Game.player_input.delete(0, END)



##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
