import os, sys, shutil

def main(arg) :
	# parent server upon which kids will be cloned
	src = r"C:\Users\OWNER\mybin\static-server"

	if len(arg) > 1 :
		dst = r"{}".format(arg[1])
		try :
			shutil.copytree(src, dst)
		except FileExistsError :
			print("A static file already exists in your destination << {} >>!".format(dst))
			print("You better get that filthy bitch outa there! xx")
			return False


		if len(arg) == 3 :
			# if all three arguments are present, remove the public directory
			# so that, the content of the third arguments can be copied into a fresh "public" dir
			# os.rmdir - hates it when its destination already exists
			os.rmdir(os.path.join(dst, "public"))

			# generate source and destination folders
			public_src = r"{}".format(arg[2])
			public_dst = os.path.join(arg[1], "public")

			# copy the static files into the public folder
			try:
				shutil.copytree(public_src, public_dst)
			except FileExistsError :
				print("A static file already exists in your destination << {} >>!".format(public_dst))
				print("You better get that filthy bitch outa there! xx")
				return False


	else :
		# if no path was passed as either 2 optional arguments
		# create a static-server on the desktop
		dst = r"C:\Users\{}\Desktop\static-server".format(os.getlogin())

		try :
			shutil.copytree(src, dst)
		except FileExistsError :
			print("A static file already exists on your desktop!")
			print("You better get that filthy bitch outa there! xx")
			return False

	print("Static Server Created Sucessfully")
		
	
if __name__ == '__main__':
	main(sys.argv)
