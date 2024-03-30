download page
https://rye-up.com/guide/installation/

rye-x86_64-windows.exe
https://github.com/astral-sh/rye/releases/latest/download/rye-x86_64-windows.exe

rye-x86-windows.exe
https://github.com/astral-sh/rye/releases/latest/download/rye-x86-windows.exe

####################

sysdm.cpl
вкладка додатково
Змінні оточення...  кнопка  Alt+з
Path 
%USERPROFILE%\.rye\shims

############################################

env var
RYE_HOME
echo %RYE_HOME%

delete
REG delete HKCU\Environment /F /V RYE_HOME

delete system (admin needed)
REG delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /F /V RYE_HOME


RYE_HOME