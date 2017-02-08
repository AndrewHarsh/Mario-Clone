@ECHO off

IF %USERPROFILE% == C:\Users\nzbq9t (
git pull
) else (
..\..\Git\bin\git pull
)

IF %ERRORLEVEL% NEQ 0 PAUSE