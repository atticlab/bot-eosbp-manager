#!/bin/sh
# Get Schedule
CONF=/opt/BP-manager/scripts/bp_manager.conf
CLEOS=/opt/EOSmainNet
PRODUSER=`cat $CONF | grep 'producer:' | awk '{print $2}'`
PRODKEY=`$CLEOS/cleos.sh get schedule | grep $PRODUSER | awk '{print $2}'`
NODE=`cat $CONF | grep $PRODKEY | awk -F "|" '{print $1}'`
NODENAME=`cat $CONF | grep $PRODKEY | awk -F "|" '{print $2}'`
NODEIP=`cat $CONF | grep $PRODKEY | awk -F "|" '{print $3}'`
echo "$PRODUSER: $PRODKEY"
echo "Node: $NODENAME $NODE $NODEIP"
