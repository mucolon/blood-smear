blood-smear: A complete repository for a prototype hematology blood smearing machine
======================
UCSD MAE 156 Spring 2019 Team 18 Project. This project involves building an automated blood smearing machine for hematology studies. A BeagleBone Black Wireless was used to control the device.

Installation
-----------------------
Clone this repository using this code below.
```
git clone git://github.com/mucolon/blood-smear.git
```

Code Methodology
--------------------------------
### Overview
A configuration file is used to declare all used GPIO pins. Then, a library is created for each motor in use. These libraries declare functions to actuate each different motor. Finally, a script is used to command all of the different motors for the automated smearing process.

### File Descriptions
The `config.py` file list all the GPIO pins being used for the blood smearing device.
The `slide_stepper.py` file declares a class with functions to actuate the linear guide's stepper motor.
The `basic_smear.py` file commands the linear guide for a Proof of Concept presentation.

References
---------------------------
I used this collection of code to built up my current repository.
```
https://github.com/mucolon/BBB/tree/master/stepper
```
