# blood-smear: A complete repository for a prototype Hematology blood smearing machine

![alt text](https://github.com/mucolon/blood-smear/blob/master/Media/Annotated_Overall_Design.png)

UCSD MAE 156 Spring 2019 Team 18 Project. This project involves building an automated blood smearing machine for Hematology studies. A BeagleBone Black Wireless, a NMEA23 stepper motor, a StepperOnline DM542T stepper motor driver, various servos, and Python 3.5.3 was used to control this device.

## Project Poster

![alt text](https://github.com/mucolon/blood-smear/blob/master/Media/Final_Poster_Presentation.png)

## Project Website

This site will become available to the public by February 2020.

[Project Website](https://sites.google.com/a/eng.ucsd.edu/156b-2019-spring-team18/home)


## Installation

Clone this repository using this code below.
```
git clone git://github.com/mucolon/blood-smear.git
```


## Code Methodology

### Overview
A configuration file is used to declare all the used pins on the BeagleBone Black Wireless. Stepper and Servo motor class libraries allows for easy setup and actuation for any number of stepper and servo motors. A GPIO input/output class library sets up pins to output 3.3V or to read binary data. A user-interface class library deals with possible terminal user inputs. Finally, a main script is used to command all of the different motors for the automated smearing process.

### Flowchart
![alt text](https://github.com/mucolon/blood-smear/blob/master/Media/Overall_Smear_Process_Flowchart.png)
This is a flowchart of the `smear.py` file.

### File Descriptions

The `smear.py` file runs the whole assembly with a GUI to make a quality blood smear.


## References

I used this collection of code to built up my current repository.

This repository contains the library used to interface with the BeagleBone's pins.
```
https://github.com/adafruit/adafruit-beaglebone-io-python
```
The repository below used the Adafruit_BBIO library to build a custom stepper motor library to actuate a stepper motor. I used this code as point to build from.
```
https://github.com/limbeckengineering/BBB
```
