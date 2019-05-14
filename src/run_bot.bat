@echo off
title RyBot V2
set /p channelname="Channel: "
python run.py -c %channelname%
pause
