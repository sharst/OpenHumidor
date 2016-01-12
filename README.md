# OpenHumidor

### Disclaimer: I am currently editing this project, therefore not all information is necessarily complete or correct.

## What is OpenHumidor?
OpenHumidor is a project consisting of both hardware and software to measure and control humidity in a cigar humidor. 
It is set up to be:
* versatile: one system fits (almost) all situations
* simple: you can set it up from the ground up within an hour or get it pre-configured
* cheap: aiming at ~10$ a sensor, ~20$ a humidifier

OpenHumidor is written in Python (base station software) and Arduino (sensor board firmware). The board layout was designed in KiCad. 

## How can I use OpenHumidor?
* With one sensor and one humidifier as a local electronic humidifying solution
* With 1-4 sensors and a receiver which displays each sensors' humidity and temperature
* With as many sensors, fans and moisturizers as you want that report to one base station:
![Three sensors, two fans and a mositurizer driven by a bases station](https://github.com/sharst/OpenHumidor/blob/master/OH-usecase1.png)

For a more detailed explanation of the components, see below. 

## Building blocks

### The sensor board
![The sensor PCB](https://github.com/sharst/OpenHumidor/blob/master/OH-sensor.jpg)

The elemental part of OpenHumidor is its sensor. It is a small (4cm x 4cm x 2cm) printed circuit board that measures air humidity and temperature. With the included wireless chip, it can transmit this data over the air to a base station. You can run the sensor either on battery or wall power. Furthermore, it is extendable via the white connectors to drive a fan, a moisturizer or communicate to any other device using a standard serial output. 

### The base station
You can use a base station to collect data from several sensors, display it or act on it. The base station uses a stripped down version of the sensor PCB to receive data from all the sensors out there. The base station itself can be any computer that is able to run Python, for instance a Raspberry Pi. 

The base station
* collects and orders data
* displays data in a simple webview that you can view from home or on the go
* if fans are available on one of the sensors, switches them on or off
* if moisturizers are available, opens or closes them
* can send you email status notifications

The webview currently looks like this (some debug informations are still being displayed):
![The OpenHumidor webview](https://github.com/sharst/OpenHumidor/blob/master/OH-webview.png)

### Moisturizer
![The moisturizer](https://github.com/sharst/OpenHumidor/blob/master/OH-moisturizer.png)

Built from a standard wooden casing and custom metal parts fabricated at [fabtools](http://www.fabtools.de). Using a stepper motor, it can be opened to varying degrees with simple commands send over a serial interface. 

### Fans
These are standard 40mm fans that run on a 5V power supply, attached to a two-pin JST plug in order to make it pluggable to the sensor board


