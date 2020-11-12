#!/bin/bash

if [ -z "$CARLA_HOME" ]; then
    echo "Please set \$CARLA_HOME before sourcing this script"
    exit 1
fi

export ROOT_SCENARIO_RUNNER=`pwd`
export CARLA_SERVER=${CARLA_HOME}/CarlaUE4.sh
CARLA_EGG=$(ls $CARLA_HOME/PythonAPI/carla/dist/carla*py3*egg)

export PYTHONPATH=$CARLA_EGG:${CARLA_HOME}/PythonAPI:${CARLA_HOME}/PythonAPI/carla/:${CARLA_HOME}/PythonAPI/carla/agents/:${ROOT_SCENARIO_RUNNER}/
