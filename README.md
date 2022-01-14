# SteamOffline

SteamOffline sets loginuser.vdf to offline mode and read only, so steam automatically starts in offline mode.

## OfflinePatch:
The OfflinePatch is a very aggressive method, but the safest.
It blocks your Steam and all it's executeable from firewall for further support.

## To revert the changes use following .bat file inside the Steam folder:
```bat
@ setlocal enableextensions 
@ cd /d "%~dp0"
if exist steam.exe (
for /R %%f in (*.exe) do (
  netsh advfirewall firewall delete rule name="Blocked: %%f" dir=out program="%%f" action=block
  netsh advfirewall firewall delete rule name="Blocked: %%f" dir=in program="%%f" action=block
)
attrib -r "config/loginusers.vdf"
)
```
