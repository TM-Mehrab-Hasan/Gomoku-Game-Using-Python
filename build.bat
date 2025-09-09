@echo off
echo Building Gomoku Game executable...
pyinstaller --onefile --windowed --name=GomokuGame --add-data="GUI_Pic;GUI_Pic" gomoku.py
echo.
echo Build complete! The executable is located at:
echo %cd%\dist\GomokuGame.exe
pause
