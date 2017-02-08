@ECHO off

SET /p Message="List the changes you made: "


IF %USERPROFILE% == C:\Users\nzbq9t (
git add "*.*"
git commit -m "%Message%"
git push origin master
) else (
..\..\Git\bin\git add "*.*"
..\..\Git\bin\git commit -m "%Message%"
..\..\Git\bin\git push origin master
)

IF %ERRORLEVEL% NEQ 0 PAUSE
