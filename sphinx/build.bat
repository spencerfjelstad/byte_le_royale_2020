@echo off

RD /S /Q "%~dp0_build"

@CALL no_touch_me.bat html

RD /S /Q "%~dp0..\docs\DisasterousGameRules"

robocopy "%~dp0_build\html" "%~dp0..\docs\DisasterousGameRules" /E /NFL /NDL /NJH /NJS /nc /ns /np

echo !!! Finished! Files moved to \docs\DisasterousGameRules !!!
echo:

pause
