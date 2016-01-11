# OpenHumidor

## What is OpenHumidor?
OpenHumidor is a project consisting of both hardware and software to measure and control humidity in a cigar humidor. 
It is set up to be:
* versatile: one system fits (almost) all situations
* simple: you can set it up from the ground up within an hour or get it pre-configured
* cheap: aiming at ~10$ a sensor, ~20$ a humidifier

## How can I use OpenHumidor?
![Three sensors, two fans and a mositurizer driven by a base station](https://github.com/sharst/OpenHumidor/blob/master/OH-usecase1.png)

## The sensor
![The sensor PCB](https://github.com/sharst/OpenHumidor/blob/master/OH-sensor.jpg)
The elemental part of OpenHumidor is its sensor. It is a small (4cm x 4cm x 2cm) printed circuit board that measures air humidity and temperature. With the included wireless chip, it can transmit this data over the air to a base station. You can run the sensor either on battery or wall power. Furthermore, it is extendable via the white connectors to drive a fan, a moisturizer or communicate to any other device using a standard serial output. 

## The base station
You can use a base station to collect data from several sensors, display it or act on it. The base station uses a stripped down version of the sensor PCB to receive data from all the sensors out there. The base station itself can be any computer that is able to run Python, for instance a Raspberry Pi. 

The base station
* collects and orders data
* displays data in a simple webview that you can view from home or on the go
* if fans are available on one of the sensors, switches them on or off
* if moisturizers are available, opens or closes them
* can send you email status notifications
