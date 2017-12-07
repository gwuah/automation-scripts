file_name = ".gitignore"

exclude = [
	"node_modules/", 
	"bin/",

	]

def gen_constants():
	return '\n'.join(sentence)

with open(file_name, "w") as gitignore :
	gitignore.write(gen_constants())
