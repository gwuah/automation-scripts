import os, subprocess

class cd:
	"""Context manager for changing the current working directory"""
	def __init__(self, newPath):
		self.newPath = os.path.expanduser(newPath)

	def __enter__(self):
		self.savedPath = os.getcwd()
		os.chdir(self.newPath)

	def __exit__(self, etype, value, traceback):
		os.chdir(self.savedPath)

path = r'C:\Program Files\MongoDB\Server\3.6\bin'

with cd(path) :
	command = "mongod.exe --dbpath /Users/Owner/mongo.data"
	subprocess.call(command.split(" "), shell=False)
