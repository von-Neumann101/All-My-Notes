@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0publish-notes.ps1"
set publish_exit=%errorlevel%
pause
exit /b %publish_exit%
