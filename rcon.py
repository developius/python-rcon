#!/usr/bin/python
# -*- coding: utf-8 -*-
import mcrcon, re, json

def cleanup(text): # because the results try to create colours and therefore have horrible characters in them
	return(text.replace("§c","").replace("§a","").replace("§6","").replace("§4","").rstrip())

class rcon:
	def __init__(self,host,port,pswd):
		try: self.r = mcrcon.MCRcon(host,port,pswd)
		except: raise Exception("Could not connect to server")
	def status(self):
		if self.__init__() == None: ok = True
		else: ok = False
		return(ok)
	def stop(self):
		return(self.r.send("stop"))
	def users(self):
		output = cleanup(self.r.send("list")).split(" ")
		return({'number':int(output[2]),'names':output[10:],'max':int(output[6])})
	def ls(self):
		return(self.users())
	def close(self):
		self.r.close()
	def cmd(self,command):
		return(self.r.send(command))
	def reload(self):
		return(self.r.send("reload"))
	def version(self):
		return(self.r.send("version"))
	def say(self,message):
		return(self.r.send("say" + str(message)))
	def save(self,mode="all"):
		return(self.r.send("save-%s" % str(mode)))
	def time(self,newTime):
		return(cleanup(self.r.send("time set %s world" % str(newTime))))
	def day(self):
		return(self.time("day"))
	def night(self):
		return(self.time("night"))
	def weather(self,newWeather):
		return(cleanup(self.r.send("weather world %s" % str(newWeather))))
	def clear(self):
		return(cleanup(self.weather("clear")))
	def op(self,user):
		return(cleanup(self.r.send("op %s" % str(user))))
	def deop(self,user):
		return(self.r.send("deop %s" % str(user)))
	def stats(self):
		output = cleanup(self.r.send("uptime"))
		stats_out = {}
		stats_out['status'] = self.status()
		stats_out['uptime'] = {'days': int(output[1]),'hours': int(output[3]),'minutes': int(output[5])}
		stats_out['TPS'] = int(str(output[9]).split("\n")[0])
		stats_out['mem'] = {'max': int(output[11]), 'allocated': int(output[14]), 'free': int(output[17])} # in MB
		stats_out['users'] = self.users()
		return(stats_out)
