blood-smear: A complete repository for a prototype Hematology blood smearing machine
======================
UCSD MAE 156 Spring 2019 Team 18 Project. This project involves building an automated blood smearing machine for Hematology studies. A BeagleBone Black Wireless, a stepper motor, a TB6600 stepper motor driver, servos, and python 3.5.3 was used to control this device.


Installation
-----------------------
Clone this repository using this code below.
```
git clone git://github.com/mucolon/blood-smear.git
```


Code Methodology
--------------------------------
### Overview
A configuration file is used to declare all the used pins on the BeagleBone Black Wireless. Stepper and Servo motor class libraries allows for easy setup and actuation for any number of stepper and servo motors. A GPIO input/output class library sets up pins to output 3.3V or to read binary data. A user-interface class library deals with possible user inputs. Finally, a main script is used to command all of the different motors for the automated smearing process.

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

The `basic_smear.py` file commands all the motors in the assembly for making a quality smear.


References
---------------------------
I used this collection of code to built up my current repository.

This repository contains the library used to interface with the Beaglebone GPIO pins.
```
https://github.com/adafruit/adafruit-beaglebone-io-python
```
The repository below used the Adafruit_BBIO library to build a custom stepper motor library to actuate a stepper motor. I used this code as point to build from.
```
https://github.com/limbeckengineering/BBB
```
