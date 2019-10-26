@echo off
del /q *.pyz

xcopy /s/e/i "game" "wrapper/game"
xcopy /s/e/i "scrimmage" "wrapper/scrimmage"
python -m zipapp "wrapper" -o "launcher.pyz"
del /q/s "wrapper/game"
del /q/s "wrapper/scrimmage"