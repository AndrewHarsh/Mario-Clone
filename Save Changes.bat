@ECHO off

SET /p Message="List the changes you made: "

..\..\Git\bin\git add "*.*"
..\..\Git\bin\git commit -m "%Message%"
..\..\Git\bin\git push origin master

IF %ERRORLEVEL% NEQ 0 PAUSE
