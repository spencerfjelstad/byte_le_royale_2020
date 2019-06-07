python -m game.scripts.generate

if /I "%1"=="true" GOTO P
if /I "%1"=="t" GOTO P
if /I "%1"=="pause" GOTO P
if /I "%1"=="p" GOTO P
if /I "%1"=="debug" GOTO P
if /I "%1"=="d" GOTO P

GOTO END

:P 

pause

:END