#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Ambrosio(object):
	"""Class for Ambrosio Personal Digital Butler

	will run our house"""
	def __init__(self):
		super(Ambrosio,self).__init__()

	def next_command(self):
		try:
			return self.cl.next()
		except:
			return None
	
	def mainloop(self):
		#while True:
		#	command = get_command
		# 	do_command(command)
		#	update
		while True:
			command = self.next_command()
			time.sleep(1)

if __name__ == "__main__":
	print "here be dragons"
