@echo off

rem set title
title System Data

rem set prompt
prompt $T

rem activate the virtual environment
call venv\Scripts\activate.bat

rem prep files
python pyexe_file_prep.py

rem run cpu script
start /B python cpu.py

rem run main script
start /B /wait python main.py

rem deactivate the virtual environment
call venv\Scripts\deactivate.bat
