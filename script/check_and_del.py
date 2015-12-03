#! /usr/bin/python
import os
import re
def scandir(startdir) :
	os.chdir(startdir)
	for obj in os.listdir(os.curdir) :
		if os.path.isdir(obj) :
			# print obj,"\n\t"
			scandir(obj)
			os.chdir(os.pardir) #!!!
		elif os.path.isfile(obj):
			m = re.match("(.*\.html)|(.*\.php)",obj)
			if m:
				print(os.path.abspath(obj))
				os.remove(obj)

startdir = raw_input('Please input startdir: ')
scandir(startdir)