@echo off
set git=D:\Programs\Git\cmd\git.exe

pushd %~dp0..

echo * Status
%git% status --porcelain


set lines=0
for /f "delims=" %%i in ('%git% status --porcelain') do set /a lines=lines+1

if %lines%==0 goto nochanges

set timestamp=%date:~10,4%-%date:~4,2%-%date:~7,2%T%time:~0,2%:%time:~3,2%:%time:~6,2%
echo * Commiting local changes: %lines%
%git% add -A --all --no-ignore-removal
%git% commit -m "Auto sync, %timestamp%"

:nochanges

echo * Status
%git% status
%git% log -1

echo * Fetch and merge

%git% fetch
%git% merge --no-edit

set lines=0
for /f "delims=" %%i in ('%git% status --porcelain') do set /a lines=lines+1

if %lines%==0 goto nonewchanges

echo * Commit again
%git% add -A --all --no-ignore-removal
%git% commit -m "commiting after merge"

:nonewchanges

echo * Push
%git% push

echo * Status
%git% status
%git% log -1

popd
goto :eof
