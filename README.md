# blood-smear: A complete repository for a prototype Hematology blood smearing machine (WIP)

![alt text](https://raw.githubusercontent.com/mucolon/blood-smear/master/Media/Annotated%20Overall%20Design.png?raw=true)

UCSD MAE 156 Spring 2019 Team 18 Project. This project involves building an automated blood smearing machine for Hematology studies. A BeagleBone Black Wireless, a stepper motor, a TB6600 stepper motor driver, servos, and Python 3.5.3 was used to control this device.

### Project Website

This site will become available to the public by Feburary 2020.

[Project Website](https://sites.google.com/a/eng.ucsd.edu/156b-2019-spring-team18/home)

## Installation

Clone this repository using this code below.
```
git clone git://github.com/mucolon/blood-smear.git
```


## Code Methodology

### Overview
A configuration file is used to declare all the used pins on the BeagleBone Black Wireless. Stepper and Servo motor class libraries allows for easy setup and actuation for any number of stepper and servo motors. A GPIO input/output class library sets up pins to output 3.3V or to read binary data. A user-interface class library deals with possible user inputs. Finally, a main script is used to command all of the different motors for the automated smearing process.

### Flowchart
![alt text](https://github.com/mucolon/blood-smear/blob/master/Media/Overall%20Smear%20Process%20Flowchart%202.0.png?raw=true)
This is a flowchart of the `basic_smear.py` file.


### File Descriptions
The `config.py` file list all the GPIO pins being used for the blood smearing device.

The `stepper.py` file declares a class with functions to actuate any stepper motor.

The `servo.py` file declares a class with functions to actuate any servo motor.

The `digital_io.py` file declares a class with functions to setup up GPIO pins as inputs or outputs.

The `ui.py` file declares a class with functions to handle all user-friendly interface.

The `test_inputs.py` file reads binary data from inductive sensors.

The `test_inputs1.py` file tests if the `read2` function in `digital_io.py` is working.

The `test_inputs2.py` file tests if sensor interrupts are working.

The `test_servo.py` file tests a servo motor's duty cycle range.

The `test_servo1.py` file tests a servo motor's rotation by angle inputs.

The `test_slide.py` file tests different motor parameters with a user-friendly interface for the linear guide's smearing process.

The `basic_smear.py` file commands all the motors in the assembly for making a quality smear. This file is shown as a flowchart above.


## References

I used this collection of code to built up my current repository.

This repository contains the library used to interface with the Beaglebone GPIO pins.
```
https://github.com/adafruit/adafruit-beaglebone-io-python
```
The repository below used the Adafruit_BBIO library to build a custom stepper motor library to actuate a stepper motor. I used this code as point to build from.
```
https://github.com/limbeckengineering/BBB
```
