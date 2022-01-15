import os
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR



filename = "config/loginusers.vdf"
os.chmod(filename, S_IWUSR|S_IREAD)

with open('config/loginusers.vdf', 'r') as file :
  filedata = file.read()

filedata = filedata.replace('"WantsOfflineMode"\t\t\"0"', '"WantsOfflineMode"\t\t\"1"')
skipWarning = '"SkipOfflineModeWarning"'
if skipWarning in filedata:
    filedata = filedata.replace('"SkipOfflineModeWarning"\t\t\"0"', '"SkipOfflineModeWarning"\t\t\"1"')
else:
    filedata = filedata.replace('"WantsOfflineMode"\t\t\"1"', '"WantsOfflineMode"\t\t\"1"\n		"SkipOfflineModeWarning"\t\t\"1"')


with open('config/loginusers.vdf', 'w') as file:
  file.write(filedata)

filename = "config/loginusers.vdf"
os.chmod(filename, S_IREAD|S_IRGRP|S_IROTH)

os.startfile('steam.exe')
