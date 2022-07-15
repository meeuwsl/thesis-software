#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
export DISPLAY=:0.0
echo $DISPLAY
cd "$parent_path"
source env/bin/activate
python main.py