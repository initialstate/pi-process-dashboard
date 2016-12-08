#!/bin/bash
# --------- User Settings ---------
PROCESS2RUN="sudo python /home/pi/grovepi/weather.py"
MONITOR_SCRIPT="/home/pi/grovepi/monitor_process.py"
# ---------------------------------
nohup $PROCESS2RUN &
VAR=`pgrep -f "$PROCESS2RUN"`
echo $VAR
nohup python $MONITOR_SCRIPT $VAR &
