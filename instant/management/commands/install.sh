#!/bin/bash

project_name=$1
base_dir=$2
project_dir=$base_dir'/'$project_name
modpath=$3
pyconf=$modpath"/genconfig.py"

cd $base_dir
source $modpath"/utils.sh"

centrifugo_version="1.7.3"
centrifugo_fetch_url="https://github.com/centrifugal/centrifugo/releases/download/v"$centrifugo_version"/centrifugo-"$centrifugo_version"-linux-386.zip"
title $yellow "1." "Downloading the websockets server"
wget $centrifugo_fetch_url
dirname="centrifugo-"$centrifugo_version"-linux-386"
unzip $dirname".zip"
check "The websockets has been downloaded"

title $yellow "2." "Installing the websockets server"
mv $dirname "centrifugo"
rm -f $dirname".zip"
sleep 1
check "The websockets server is installed"

title $yellow "3." "Configuring websockets server"
echo "Generating Centrifugo config"
cd centrifugo
./centrifugo genconfig
echo "Updating Django settings"
python3 $pyconf $project_name $base_dir ok
check "Websockets server config generated and settings updated."

ok $green "The Centrifugo websockets server is installed. Run it with python3 manage.py runws"

exit 0
