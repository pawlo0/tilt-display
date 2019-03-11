# tilt-display

My tentative of using 8-digit display [Raspeberry Pi Zeroseg](https://thepihut.com/products/zeroseg) to monitor beer fermentation using [Tilt Wireless Hydrometer](https://tilthydrometer.com/)

## step 1: Download Image
Download [Raspeberry Pi SD image for Tilt](https://tilthydrometer.com/products/tilt-pi-raspberry-pi-disk-image-download).

There are more options, like installing the Tilt Pi monitoring app in a fresh Raspbian Jessie or Stretch from [baronbrew](https://github.com/baronbrew/TILTpi), but for the sake of simplicity, I started with an image already prepared to work with the Tilt.

## step 2: Update and upgrade
Boot (power on) your Raspberry Pi, in a new terminal window, update Raspbian:

`sudo apt-get update`

`sudo apt-get upgrade`

## step 3: Enable SPI
Run the configuration tool by entering the following command and hitting enter:

`sudo raspi-config`

When the tool opens, go to option 5 ‘Interfacing Options’ and press enter. Then highlight option 4 ‘SPI’ and press enter.
Select Yes to enable the SPI interface and hit enter. Exit the config tool by selecting Finish.

## step 4: Reboot your Raspberry Pi

`sudo reboot`

## step 5: Install essentials
Once rebooted, install some required bluetooth and python software
 
`sudo apt-get install bluez python-bluez python-requests python-pygame python-rpi.gpio git build-essential python-dev python-pip`

## step 6: Check That the Pi Can See the Tilt
Drop your Tilt Hydrometer in a glass of water and type the following command in a terminal.

`sudo hcitool lescan`

When you see the tilt address and name pop up hit ctrl + c to stop the scan. The 12 digit hexadecimal number is the bluetooth address of the tilt. If it does not appear, check your Tilt's battery status, if it is actually turning on (LED flashs when tilt is moved from vertical position to angled position). Try checking with an Android or IOS device. If the Tilt is OK, then there must be something wrong with the RPi. Double check all the required bluetooth software is installed.

# step 7: Set Up the Python Code
