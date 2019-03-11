# tilt-display

My tentative of using 8-digit display [Raspeberry Pi Zeroseg](https://thepihut.com/products/zeroseg) to monitor beer fermentation using [Tilt Wireless Hydrometer](https://tilthydrometer.com/)

1.Download [Raspeberry Pi SD image for Tilt](https://tilthydrometer.com/products/tilt-pi-raspberry-pi-disk-image-download)
There are more options, like installing the Tilt Pi monitoring app in a fresh Raspbian Jessie or Stretch from [baronbrew](https://github.com/baronbrew/TILTpi), but for the sake of simplicity, I started with an image already prepared to work with the Tilt.

2. Upgrade and update
Boot (power on) your Raspberry Pi, in the terminal window, update Raspbian:
`sudo apt-get update`
`sudo apt-get upgrade`

3.Enable SPI
Run the configuration tool by entering the following command and hitting enter:
`sudo raspi-config`
When the tool opens, go to option 5 ‘Interfacing Options’ and press enter. Then highlight option 4 ‘SPI’ and press enter.
Select Yes to enable the SPI interface and hit enter. Exit the config tool by selecting Finish.

4.Reboot your Raspberry Pi
`sudo reboot`

5.Install essentials
Once rebooted, install some required bluetooth and python software
`sudo apt-get install bluez python-bluez python-requests python-pygame python-rpi.gpio git build-essential python-dev python-pip`

