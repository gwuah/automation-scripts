file_name = ".gitignore"

exclude = [
	"node_modules/", 
	"bin/",

	]

def gen_constants():
	constants = ""
	for misc in exclude :
		constants += "{}\n".format(misc)
	return constants

with open(file_name, "w") as gitignore :
	gitignore.write(gen_constants())
