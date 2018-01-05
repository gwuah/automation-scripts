import os
import sys

class cd:
	"""Context manager for changing the current working directory"""
	def __init__(self, newPath):
		self.newPath = os.path.expanduser(newPath)

	def __enter__(self):
		self.savedPath = os.getcwd()
		os.chdir(self.newPath)

	def __exit__(self, etype, value, traceback):
		os.chdir(self.savedPath)


def gen_constants():
	exclude = [
	"node_modules/", 
	"bin/",
	]

	return '\n'.join(exclude)

def create_file(filename, mode, data=None) :
	if not data :
		with open(filename, mode) as temp :
			temp.close()
	else :
		with open(filename, mode) as temp :
			temp.write(data)
			temp.close()
	return True


def main(arg) :
	if len(arg) > 1 :
		folder_name = arg[1]
	else :
		folder_name = "casprina-folder"
		
	source_folder_name = "src"
	index_filename = "index.js"
	css_filename = "main.css"
	gitignore = ".gitignore"


	try :
		
		# create project folder
		os.mkdir(folder_name)

		# change directory into project folder
		with cd(folder_name):

			# create source folder
			os.mkdir(source_folder_name)

			# enter src folder
			with cd(source_folder_name) :

				# create js folder 
				os.mkdir("js")
				
				# enter js folder 
				with cd("js") :

					# enter your code here
					create_file(index_filename, "w")

				# create css folder
				os.mkdir("css")
				
				# navigate into css folder
				with cd("css") :
					
					# enter code here
					create_file(css_filename, "w")

			# generate index.html
			create_file("index.html", "w")

			# generate gulpfile.js
			create_file("gulpfile.js", "w")

			# generate gitignore
			create_file(gitignore, "w", gen_constants())


	except FileExistsError :
		print("the file you're trying to create already exists in your current location")

if __name__ == '__main__':
	main(sys.argv)
