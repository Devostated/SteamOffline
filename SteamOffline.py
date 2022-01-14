import os
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR



filename = "config/loginusers.vdf"
os.chmod(filename, S_IWUSR|S_IREAD)

with open('config/loginusers.vdf', 'r') as file :
  filedata = file.read()

filedata = filedata.replace('"WantsOfflineMode"		"0"', '"WantsOfflineMode"		"1"')
skipWarning = '"SkipOfflineModeWarning"'
if skipWarning in filedata:
    filedata = filedata.replace('"SkipOfflineModeWarning"		"0"', '"SkipOfflineModeWarning"		"1"')
else:
    filedata = filedata.replace('"WantsOfflineMode"		"1"', '"WantsOfflineMode"		"1"\n		"SkipOfflineModeWarning"		"1"')


with open('config/loginusers.vdf', 'w') as file:
  file.write(filedata)

filename = "config/loginusers.vdf"
os.chmod(filename, S_IREAD|S_IRGRP|S_IROTH)

os.startfile('steam.exe')