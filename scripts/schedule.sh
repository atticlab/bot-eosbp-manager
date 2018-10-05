#!/bin/sh
# Get Schedule
CONF=/opt/BP-manager/scripts/bp_manager.conf
CLEOS=`cat $CONF | grep 'cleos:' | awk '{print $2}'`
PRODUSER=`cat $CONF | grep 'producer:' | awk '{print $2}'`

ACTIVEPRODKEY=`$CLEOS/cleos.sh get schedule | grep -A20 'active schedule' | grep $PRODUSER | awk '{print $2}'`

if [ -n "$ACTIVEPRODKEY" ]
then
	ACTIVENODE=`cat $CONF | grep $ACTIVEPRODKEY | awk -F "|" '{print $1}'`
	ACTIVENODENAME=`cat $CONF | grep $ACTIVEPRODKEY | awk -F "|" '{print $2}'`
	ACTIVENODEIP=`cat $CONF | grep $ACTIVEPRODKEY | awk -F "|" '{print $3}'`
fi

PROPOSEDPRODKEY=`$CLEOS/cleos.sh get schedule | grep -A20 'proposed schedule' | grep $PRODUSER | awk '{print $2}'`

if [ -n "$PROPOSEDPRODKEY" ]
then
	PROPOSEDNODE=`cat $CONF | grep $PROPOSEDPRODKEY | awk -F "|" '{print $1}'`
	PROPOSEDNODENAME=`cat $CONF | grep $PROPOSEDPRODKEY | awk -F "|" '{print $2}'`
	PROPOSEDNODEIP=`cat $CONF | grep $PROPOSEDPRODKEY | awk -F "|" '{print $3}'`
fi

if [ -n "$ACTIVEPRODKEY" ]
then
	echo "Active schedule:"
	echo "$PRODUSER: $ACTIVEPRODKEY"
	echo "Node: $ACTIVENODENAME $ACTIVENODE $ACTIVENODEIP"
fi

if [ -n "$PROPOSEDPRODKEY" ]
then
	echo "Proposed schedule:"
	echo "$PRODUSER: $PROPOSEDPRODKEY"
	echo "Node: $PROPOSEDNODENAME $PROPOSEDNODE $PROPOSEDNODEIP"
fi
