
del /s/q _build

call make.bat html

rmdir /s/q "../docs/DisasterousGameRules"
md "../docs/DisasterousGameRules"
xcopy /s/e/i "_build/html" "../docs/DisasterousGameRules"

pause