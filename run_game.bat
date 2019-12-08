@echo off
call .\build.bat
python .\launcher.pyz generate
python .\launcher.pyz run
python .\launcher.pyz visualizer
