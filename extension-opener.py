import os

path = r'C:\Users\{}\AppData\Local\Google\Chrome\User Data\Default\Extensions'.format(os.getlogin())
extensionId = input("Extension id :> ")

os.startfile(os.path.join(path, extensionId))