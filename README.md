blood-smear: A complete repository for a prototype Hematology blood smearing machine
======================
UCSD MAE 156 Spring 2019 Team 18 Project. This project involves building an automated blood smearing machine for hematology studies. A BeagleBone Black Wireless, stepper motors, TB6600 stepper motor drivers, and python 3.5.3 was used to control this device.


Installation
-----------------------
Clone this repository using this code below.
```
git clone git://github.com/mucolon/blood-smear.git
```


Code Methodology
--------------------------------
### Overview
A configuration file is used to declare all the used GPIO pins. A stepper motor class library allows for easy setup and actuation for any number of stepper motors. A GPIO input class library sets up and reads pins. A user-interface class library deals with possible user inputs. Finally, a main script is used to command all of the different motors for the automated smearing process.

### File Descriptions
The `config.py` file list all the GPIO pins being used for the blood smearing device.

The `stepper.py` file declares a class with functions to actuate any stepper motor.

The `input_io.py` file declares a class with functions to setup up pins as inputs.

The `ui.py` file declares a class with functions to handle all user-friendly interface.

The `test_inputs.py` file tests if the `input_io.py` library is working correctly.

The `test_slide.py` file tests different motor parameters with a user-friendly interface for the linear guide's smearing process.

The `basic_smear.py` file commands the linear guide for a Proof of Concept presentation.


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
