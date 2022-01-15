# SteamOffline
SteamOffline sets loginuser.vdf to offline mode and read only, so the Steam client automatically starts in offline mode.

## OfflinePatch:
The OfflinePatch is a very aggressive method, but the safest.
It blocks your Steam and all it's executeables by the firewall for further support.

## Download
The download can be found on the [Release](https://github.com/Devostated/SteamOffline/releases) page.

## Usage
- install a second Steam client
- login and install games you want to run offline
- close Steam
- place the SteamOffline.exe and OfflinePatch.exe into your new Steam folder
- run SteamOffline.exe or OfflinePatch.exe if you want to Steam to be blocked by your firewall
- you can keep using steam.exe or SteamOffline.exe. SteamOffline.exe just makes sure that the loginuser.vdf is still in read only and has the correct parameters.



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
