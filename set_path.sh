#!/bin/bash

if [ -z "$CARLA_HOME" ]; then
    echo "Please set \$CARLA_HOME before sourcing this script"
    exit 1
fi

# Get the carla version.
CARLA_VERSION=$(cat $CARLA_HOME/VERSION)
if [ -z "$CARLA_VERSION" ]; then
    echo "Please set \$CARLA_VERSION before sourcing this script"
    exit 1
fi

export ROOT_SCENARIO_RUNNER=`pwd`
export CARLA_SERVER=${CARLA_HOME}/CarlaUE4.sh

if [ $CARLA_VERSION = "0.9.9" ] ; then
    PYTHON_VER=3.7
else
    PYTHON_VER=3.5
fi

export PYTHONPATH=${CARLA_HOME}/PythonAPI/carla/dist/carla-$CARLA_VERSION-py$PYTHON_VER-linux-x86_64.egg:${CARLA_HOME}/PythonAPI:${CARLA_HOME}/PythonAPI/carla/:${CARLA_HOME}/PythonAPI/carla/agents/:${ROOT_SCENARIO_RUNNER}/
