import labirinthe
import os

class Perso(object):
	def __init__(self):
		self.position=()

	def id(self,tab):
		if 1 in tab.values():
			self.id==1
		if 2 in tab.values():
			self.id==2
	def positions(self, tab):
		for i,v in tab.items():
			if v == 1 :
				print(i)
		