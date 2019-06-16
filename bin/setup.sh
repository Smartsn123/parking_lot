#!/bin/bash
VERSION=1.0
echo "Building ParkingLotApp version "$VERSION
MY_PATH="`dirname \"$0\"`"              # relative
MY_PATH="`( cd \"$MY_PATH\" && pwd )`"  # absolutized and normalized
if [ -z "$MY_PATH" ] ; then
  # error; for some reason, the path is not accessible
  # to the script (e.g. permissions re-evaled after suid)
  exit 1  # fail
fi
#echo $MY_PATH
cd $MY_PATH/../
apt-get install python python-pip
pip install -r requirements.txt
python tests/test_main.py -v
cp bin/parking_lot.sh bin/parking_lot_tmp.sh
chmod +x bin/parking_lot_tmp.sh
mv bin/parking_lot_tmp.sh bin/parking_lot
echo "Setup done Successfully!"