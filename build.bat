@echo off
del /q *.pyz

xcopy /s/e/i "game" "wrapper/game"
python -m zipapp "wrapper" -o "launcher.pyz"
del /q/s "wrapper/game"