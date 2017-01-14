@ECHO off

SET /p Message="List the changes you made: "

git add "*.*"
git commit -m "%Message%"
git push origin master

IF %ERRORLEVEL% NEQ 0 PAUSE
