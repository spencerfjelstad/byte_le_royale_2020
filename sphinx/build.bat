@echo off

RD /S /Q "%~dp0_build"

@CALL no_touch_me.bat html

RD /S /Q "%~dp0..\docs\documentation~"

robocopy "%~dp0_build\html" "%~dp0..\docs\documentation~" /E /NFL /NDL /NJH /NJS /nc /ns /np

echo !!! Finished! Files moved to \docs\documentation~ !!!
echo:

pause
