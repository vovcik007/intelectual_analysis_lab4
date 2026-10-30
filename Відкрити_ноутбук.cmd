@echo off
cd /d "%~dp0"
".venv\Scripts\python.exe" launch_lab.py --notebook
if errorlevel 1 pause
