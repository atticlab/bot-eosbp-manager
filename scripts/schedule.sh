#!/bin/sh
# Get Schedule
SCHED=`cat /opt/EOSmainNet/scripts/schedule.conf`
echo $SCHED
#PROD=`echo $SCHED | grep 'produser:' | awk '{print $1}'`
PROD=`echo $SCHED | grep 'site:'`
echo $PROD
