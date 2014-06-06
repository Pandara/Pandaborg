#!/usr/bin/python

###################################
# Run Script in Debug mode?
debug = True
# Set it to false if you don't need it!
###################################

# Import some necessary libraries.
import socket
import time
import platform
password = raw_input("Please input password: ")
ChanPass = raw_input("Please input the channel password: ")


####################################
# IRC Interface:                   #
# This is the primary mode of      #
# communication with Aigis         #
####################################
class ircInterface:

  # Some basic variables used to configure the bot
  server = "irc.rizon.net" # Server
  channelsToJoin = ["#kawayui", "#hajime", "#nyaa-nyaa",  "#nyaa-ni", "#nyaa-lewd", "#navypandas", "#bots"]
  channelsToJoin_pass = [ChanPass, "", "", "","","",""]
  botnick = "Pandaborg" # Your bots nick
  owner = "Pandara"

  nickServPass = password
  ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  connected = True

  connectedChannels = []

  def __init__(self, inServer = server, inNick = botnick, nsIn = nickServPass):
    self.server = inServer
    self.botnick =  inNick
    self.nickServPass = nsIn

    self.ircsock.connect((self.server, 6667)) # Here we connect to the server using the port 6667
    self.ircsock.send("USER "+ "Pand" +" "+ self.botnick +" "+ self.botnick +" :Pandaborg\n") # user authentication
    self.ircsock.send("NICK "+ self.botnick +"\n") # here we actually assign the nick to the bot
    self.authNickServ()



    while self.connected:
      ircmsg = self.ircsock.recv(2048) # receive data from the server
      ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.

      ###### Parse like no tomorrow ##########
      name = ircmsg[ircmsg.find(":")+1:ircmsg.find("!")]
      message = ircmsg[ircmsg.find(":",2)+1:]
      if ircmsg.find("PRIVMSG") != -1:
        origin = ircmsg[ircmsg.find("PRIVMSG",2)+8:ircmsg.find(":",2)]
      else:
        origin = "Server Msg"

      ####### Print some readable data ############
      if debug:
        print(ircmsg)
        print("Name: "+name+"; Message: " + message +"; Origin: " + origin)
      else:
        print("<"+name+"> " + message)

      ###### Events #########

      if ircmsg.find("If you do not change within one minute, I will change your nick.") != -1:
        self.authNickServ()

      if ircmsg.find("Password accepted - you are now recognized") != -1:
        self.sendmsg(self.owner, self.botnick + " Console Initiated.")
        self.sendmsg(self.owner, self.owner+"@"+self.botnick+":/")
        self.joinDefaultChannels() # Join the channel using the functions we previously defined

      if ircmsg.find(":Hello "+ self.botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
        self.sendmsg(origin, "Hello " + name +"~")

      if ircmsg.find("\x01ACTION") != -1 and name == "ZCool" != -1 and ircmsg.find("flops") != -1 and ircmsg.find(self.botnick) != -1: # Reply to ZCool flopping on lap
        time.sleep(1)
        self.sendaction(origin, "pets " + name + "~")

      if ircmsg.find("\x01ACTION flops onto " + self.botnick + "'s lap") != -1 and name != "ZCool": # Reply to people flopping on lap
        time.sleep(1)
        self.sendaction(origin, "pets " + name + "~")

      if message.lower() == ("no u") and name == "Pepper-Sensei": # Be aggressive to Peppity Pep
        time.sleep(1)
        self.sendmsg(origin, "U startin lyk Pepper?")

      if message.lower() == ("bored") and name == "Pepper-Sensei": # Tell Pepper to do things
        time.sleep(1)
        self.sendmsg(origin, "Then do something " + name + "~")

#      if name == "Midori" and ircmsg.lower().find("lewd") != -1: # Tell Midori she's lewd
#        time.sleep(1)
#        self.sendmsg(origin, "But you're the lewdest " + name + "~")

      if name == "Pandara" and ircmsg.lower().find("who is the lewdest of them all") != -1: # Explain who is lewd
        time.sleep(1)
        self.sendmsg(origin, "Midori, of course~")

#      if name == "buenouanq" and ircmsg.lower().find("free") != -1: # Telling bueno the facts
#	      time.sleep(1)
#	      self.sendmsg(origin, "You're a faget")

      if name == "I_can_FLY" and ircmsg.lower().find("gun") != -1:# Telling Fly the facts
        time.sleep(1)
        self.sendmsg(origin, "3>Liking guns")
        time.sleep(1)
        self.sendmsg(origin, "You must have a small penis")
        time.sleep(1)
        self.sendmsg(origin, "And man boobs.")



		###############################
		##### Ping Pong Circulate #####
		###############################
      if message.lower() == ("ping"):
        time.sleep(1)
        self.sendmsg(origin, "Pong")
        time.sleep(1)
        self.sendmsg(origin, "Circulate")
		###############################
		##### Ping Pong Circulate #####
		###############################


      if message.lower() == ("morning"): # Replies to people saying morning
        time.sleep(1)
        self.sendmsg(origin, "Good morning " + name + "~ How are you~?")

      if ircmsg.lower().find("pls") != -1 or ircmsg.lower().find("p\x01ls") != -1 or ircmsg.lower().find("pl\x01s") !=-1:
        time.sleep(1)
        self.sendmsg(origin, "*please")

      if ircmsg.lower().find("pandas") != -1 and ircmsg.lower().find("navypandas") == -1 and name != "Pandara":
        time.sleep(1)
        self.sendmsg(origin, "Did someone say pandas?")
        time.sleep(1)
        self.sendmsg(origin, name + " do you wish to make a contract and join the panda army?")
        self.ircsock.send ("INVITE " + name + " :#navypandas\n");

#      if ircmsg.find(":ping") != -1: # Replies to people saying good morning
#        self.sendmsg(origin, "Dicks")

      if ircmsg.lower().find("*whips out dick*") != -1 or ircmsg.lower().find("*unzips dick") != -1: # Lewd things general
	      time.sleep(1)
	      self.sendmsg(origin, "How very lewd " + name)

      if ircmsg.lower().find("you don't even monkey") != -1: # Let's people know that monkeying is important
	      time.sleep(1)
	      self.sendmsg(origin, "3>She doesn't even monkey")

      if ircmsg.lower().find("doesn't even monkey") != -1: # Let's people know that monkeying is important
        time.sleep(1)
        self.sendmsg(origin, "3>She doesn't even monkey")

      if ircmsg.lower().find("do you even monkey?") != -1: # Let's people know that monkeying is important
	      time.sleep(1)
	      self.sendmsg(origin, "3>2014 >Not monkeying")

      if ircmsg.lower().find("\x01action dances with " + self.botnick.lower()) !=-1: # Let's dance
        time.sleep
        self.sendaction(origin, "dances with " + name + "~")

      if ircmsg.lower().find(self.botnick.lower() + ", talk dirty to me") != -1: # When. You. Talk dirty to me.
        time.sleep(1)
        self.sendaction(origin, "talks dirty to " + name)

      if ircmsg.lower().find("keikaku") != -1: # All according to keikaku
	      time.sleep(1)
	      self.sendmsg(origin, "2TL Note: Keikaku means plan")

      if ircmsg.find("JOIN") != -1 and name == "Aigis": # Kiss Aigis when she joins
        time.sleep(1)
        self.sendaction(message.replace(" ",""), "kisses " + name + "~")

      if ircmsg.find("\x01ACTION kisses Pandaborg, holds her hand, and sits down with her~") != -1 and name == "Aigis":
        time.sleep(1)
        self.sendaction(origin, "nuzzles " + name + "~")

#      if ircmsg.find("\x01ACTION hugs " + self.botnick) != -1 and name != "Aigis": # Hugs everyone except Aigis to avoid looping
#        time.sleep(1)
#        self.sendaction(origin, "hugs " + name + "~")

      if ircmsg.lower().find("\x01action hugs " + self.botnick.lower()) != -1 and name != "Aigis" and name != "KugelBlitz":
        time.sleep(1)
        self.sendaction(origin, "hugs " + name + "~")

      if ircmsg.lower().find("\x01action pets " + self.botnick.lower()) != -1: # Reply to pets
        self.sendaction(origin, "nuzzles " + name + "~")

      if ircmsg.find("\x01ACTION hugs " + self.botnick) != -1 and name == "Aigis": # Kiss Aigis when hugged by her
	      self.sendaction(origin, "kisses " + name + "~")

      if name == self.owner and message.find("\x01ACTION snaps her fingers") != -1: # Quit commands
	      self.quitIRC()

      if name == self.owner and ircmsg.lower().find("say goodnight " + self.botnick.lower()) != -1: # Quit commands
        time.sleep(1)
        self.sendmsg(origin, "Goodnight " + self.botnick)
        self.quitIRC2()

  #    if ircmsg.lower().find("join ") != -1 and name == self.owner and origin == self.botnick:
  #      self.joinchan(ircmsg[ircmsg.find("#")-1:], "")

  #    if ircmsg.lower().find("leave ") != -1 and name == self.owner and origin == self.botnick:
  #      self.partchan(ircmsg[ircmsg.find("#")-1:])

      if name == self.owner and message.find(self.botnick + ", go the fuck to sleep") != -1: # Quit commands
        time.sleep(1)
        self.sendmsg(origin, "Fine.")
        self.quitIRC2()

      if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
        self.ping()

      if name == self.owner and origin == self.botnick + " ":
        self.processConsoleReq(message)

      ## CTCP
      if message.find("VERSION") !=-1:
        self.respondVersion(name)


  def respondVersion(self, name):
    if debug:
      print("replying to " + name + " with VERSION with:")
      print("NOTICE "+ name + " :" + "Pandaborg, the next generation cybernetic panda, running " + platform.uname()[0] + " on " + platform.uname()[5])

    self.ircsock.send("NOTICE "+ name + " :" + "Pandaborg, the next generation cybernetic panda, running " + platform.uname()[0] + " on " + platform.uname()[5]+"\n")

  def ping(self): # Reply to Server PINGs
    self.ircsock.send("PONG :circulate\n")

  def processConsoleReq(self, command): ## TODO:  SENDACTION"
    responce = "Nothing preformed. Check your syntax and try again. If you forgot what you programmed type 'HELP'."
    action = command.split()
    if debug:
      print(action)

    if action[0].find("HELP") != -1:
      responce = "Available Commands: HELP, JOINCHAN, LEAVECHAN, QUIT, SENDMSG, SENDALL"

    elif action[0].find("JOINCHAN") != -1:
      if len(action) > 2:
        self.joinchan(action[1],action[2])
        responce = "Joining requested channel!"
      elif len(action) > 1:
        self.joinchan(action[1])
        responce = "Joining requested channel!"
      else:
        responce = "Not enough arguments. JOINCHAN #[channel] ([password])"

    elif action[0].find("LEAVECHAN") != -1:
      if len(action) > 1:
        self.leavechan(action[1])
        responce = "Left requested channel!"
      else:
        responce = "Not enough arguments. LEAVECHAN #[channel]"
    elif action[0].find("QUIT") != -1:
      self.quitIRC()

    elif action[0].find("SENDMSG") != -1:
      if len(action) > 2:
        self.sendmsg(action[1],self.joinArgForSend(action[2:]))
        responce = "Message sent!"
      else:
        responce = "Not enough arguments. SENDMSG [target] [message]"

    elif action[0].find("SENDALL") != -1:
      if len(action) > 1:
        self.sendmsgall(self.joinArgForSend(action[1:]))
        responce = "Sent message to all connected channels!"
      else:
        responce = "Not enough arguments. SENDALL [message]"

    elif action[0].find("SENDACTION") != -1:
      if len(action) > 2:
        self.sendaction(action[1],self.joinArgForSend(action[2:]))
        responce = "Sent action to channel!"
      else:
        responce = "Not enough arguments. SENDACTION [target] [message]"
    self.sendmsg(self.owner, responce)

  def sendmsgall(self, msg):
    for joinedChan in self.connectedChannels:
      self.sendmsg(joinedChan, msg)

  def joinArgForSend(self, messageArray):
    return " ".join(messageArray);

  def sendmsg(self, chan , msg): # This is the send message function, it simply sends messages to the channel.
    self.ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")

  def sendaction(self, chan, action): # Lights? Camera? ACTION!
    self.sendmsg(chan, "\x01ACTION " + action + "\x01")

  def quitIRC(self): # Quit definition and message
    self.ircsock.send("QUIT :Shutting down, Pandara-sama.\n")
    self.connected = False
    self.ircsock = None
    self = None

  def quitIRC2(self): # Quit definition and message
    self.ircsock.send("QUIT :Entering sleep mode Pandara-sama\n")
    self.connected = False
    self.ircsock = None
    self = None

  def joinchan(self, chan, cpass = ""): # This function is used to join channels.
    self.connectedChannels.append(chan)
    self.ircsock.send("JOIN "+ chan + " " + cpass +"\n")

  def leavechan(self, chan): # This function is used to join channels.
    self.connectedChannels.remove(chan)
    self.ircsock.send("PART "+ chan +"\n")

  def joinDefaultChannels(self):
    for (i, tojoin) in enumerate(self.channelsToJoin):
      self.joinchan(tojoin,self.channelsToJoin_pass[i])

  def authNickServ(self):
    self.ircsock.send("PRIVMSG NickServ :"+ "identify " + self.nickServPass +"\n")

#  def joinchan(self, chan, cpass): # This function is used to join channels.
#    self.ircsock.send("JOIN "+ chan + " " + cpass +"\n")

  def partchan(self, chan): # This function is used to join channels.
    self.ircsock.send("PART "+ chan +"\n")

  def help(self):
    self.ircsock.send("PRIVMSG "+ self.channel +" :No")

#  def hello(self): # This function responds to a user that inputs "Hello Mybot"
#    self.ircsock.send(self.origin +" :Hello!\n")

#  def pet(self):
#	self.ircsock.send("PRIVMSG "+ self.channel +" /me nuzzles !\n")

####################################
# Bot  :                           #
# The bot's starting point.        #
####################################

class Bot:
  def __init__(self):
    print("IRC Bot System starting...")
    self.main()

  def main(self):
    RizonInterface = ircInterface()

LocalBot = Bot()
