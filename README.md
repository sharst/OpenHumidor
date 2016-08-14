# OpenHumidor

## What is OpenHumidor?
OpenHumidor is a project consisting of both hardware and software to measure and control humidity in a cigar humidor. 
It is set up to be:
* versatile: one system fits (almost) all situations
* simple: you can set it up from the ground up within an hour or get it pre-configured
* cheap: aiming at ~10$ a sensor, ~20$ a humidifier

OpenHumidor is written in Arduino. The board layout was designed in KiCad. There is also an interface for python. OpenHumidor is spread over several GitHub repositories, so you only need to check out the files you actually need. 
* [OpenHumidor-Arduino](https://github.com/sharst/OpenHumidor-Arduino) for the sensor board firmware
* [OpenHumidor-Hardware](https://github.com/sharst/OpenHumidor-Hardware) for the sensor layout files
* This repository, where I will release the Python code and tools once they are ready. 

## How can I use OpenHumidor?
* With one sensor and one humidifier as a local electronic humidifying solution. 
<img src="https://github.com/sharst/OpenHumidor/blob/master/wiki_images/OH-usecase-single.png" width=50 align="right">

The sensor will measure relative humidity and open the moisturizer should the air be too dry.
 

* With 1-4 sensors and a base station which displays each sensors' humidity and temperature
<img src="https://github.com/sharst/OpenHumidor/blob/master/wiki_images/OH-usecase-base.png"  width=200 align="right">

The sensors will transmit humidity and temperature data to a base station, which displays the data. Additionally, you can add fans and moisturizers to the sensors. The base station will decide based on the data whether to switch on fans or open the air humidifiers.

.

.

* With as many sensors as you like, connected to your computer
<img src="https://github.com/sharst/OpenHumidor/blob/master/wiki_images/OH-usecase-pc.png"  width=200 align="right">

Same as in the example above, but the data will be transmitted to your computer or any other device that support serial data transfer. Develop your own cool ways of reacting to humidity changes. There's a handy python library available for quick integration.

For a more detailed explanation of the components, see below. 

## Where can I buy it?
Currently, nowhere. Once I'm ready with all the testing I will howerver try to provide pre-assembled boards. In the meantime, you can build your own by following the [getting started guide](https://github.com/sharst/OpenHumidor/wiki/Getting-Started-With-OpenHumidor)
I would however be very greatful if you signaled you interest by watching this project. This way you'll stay up to date with the progress in this project. You can always get an overview of the project status in the [wiki](https://github.com/sharst/OpenHumidor/wiki).

## How can I get involved?
Some ideas:
* Watch this project to show me you're interested
* Build your own OpenHumidor system and report back to me if you run into problems
* If you have any questions, send me a message
* Browse the source code
* File issues or enhancement requests
* Fork the project, make my code better and file a pull request!
* Solve one of the issues in the bug tracker!

## Building blocks

### The sensor board
![The sensor PCB](https://github.com/sharst/OpenHumidor/blob/master/wiki_images/board_v06.jpg)

The elemental part of OpenHumidor is its sensor. It is a small (4cm x 4cm x 2cm) printed circuit board that measures air humidity and temperature. With the included wireless chip, it can transmit this data over the air to a base station. You can run the sensor either on battery or wall power. Furthermore, it is extendable via the white connectors to drive a fan, a moisturizer or communicate to any other device using a standard serial output. 

### The base station
You can use a base station to collect data from several sensors, display it and act on it. The base station uses a stripped down version of the sensor PCB to receive data from all the sensors out there.

The base station
* collects and orders data
* displays data on a 2.2" tft display
* if fans are available on at least one of the sensors, switches them on or off
* if moisturizers are available, opens or closes them


### Moisturizer
![The moisturizer](https://github.com/sharst/OpenHumidor-Hardware/blob/master/Humidifier/humidifier_3dprint_overview.png)

Built from a standard wooden casing and custom metal parts fabricated at [fabtools](http://www.fabtools.de). Using a servo motor, it can be opened when the surrounding air is too dry.

### Fans
These are standard 40mm fans that run on a 5V power supply, attached to a two-pin JST plug in order to make it pluggable to the sensor board. These are switched on if there is a significant humidity difference between at least two sensors. The air will start to move in your cigar cabinet and even out any moisture differences.

### UART connector for your convenience
You want to use OpenHumidor for something entirely different? All data from the sensors is available to you either directly from the sensors or from the base station by means of a simple, open protocol. There is even a python library to get you started!


