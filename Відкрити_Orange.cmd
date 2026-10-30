@echo off
cd /d "%~dp0"
".venv\Scripts\python.exe" launch_lab.py --orange
if errorlevel 1 pause
