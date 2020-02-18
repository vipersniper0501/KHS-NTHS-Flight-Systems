#!/bin/bash
#Run this in terminal
g++ -std=c++14 today.cpp -o a.out
mkdir /etc/Moore_Flight_Computer/
mv balloon.sh /etc/init.d/
chmod +x /etc/init.d/balloon.sh
mv a.out /etc/Moore_Flight_Computer/
mv data.sh /etc/Moore_Flight_Computer/
mv camera.sh /etc/Moore_Flight_Computer/
exit 0
