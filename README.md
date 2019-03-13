# tilt-display

My tentative of using 8-digit display [Raspeberry Pi Zeroseg](https://thepihut.com/products/zeroseg) to monitor beer fermentation using [Tilt Wireless Hydrometer](https://tilthydrometer.com/)

## step 1: Download Image
Download [Raspeberry Pi SD image for Tilt](https://tilthydrometer.com/products/tilt-pi-raspberry-pi-disk-image-download).

There are more options, like installing the Tilt Pi monitoring app in a fresh Raspbian Jessie or Stretch from [baronbrew](https://github.com/baronbrew/TILTpi), but for the sake of simplicity, I started with an image already prepared to work with the Tilt.

## step 2: Update and upgrade
Boot (power on) your Raspberry Pi, in a new terminal window, update Raspbian:

`sudo apt-get update`

`sudo apt-get upgrade`

Had some errors during the upgrade, due to being unable to fetch some archives. But running it again with `--fix-missing` option fixed the problem. I.e. `sudo apt-get upgrade --fix-missing`.

## step 3: Enable SPI
Run the configuration tool by entering the following command and hitting enter:

`sudo raspi-config`

When the tool opens, go to option 5 ‘Interfacing Options’ and press enter. Then highlight option 4 ‘SPI’ and press enter.
Select Yes to enable the SPI interface and hit enter. Exit the config tool by selecting Finish.

## step 4: Reboot your Raspberry Pi

`sudo reboot`

## step 5: Install essentials
Once rebooted, install some required bluetooth and python software
 
`sudo apt-get install git build-essential python-bluez python-requests python-pygame python-rpi.gpio python-dev python-pip`

# step 7: Install Zeroseg
Enter `cd~` in the terminal and hit enter, to ensure you're in the home directory

Next clone the Zeroseg code library:

`git clone https://github.com/AverageMaker/ZeroSeg.git`

Enter your new ZeroSeg directory (case sensitive)

`cd ZeroSeg`

Run the following command to install the Zeroseg library:

`sudo python setup.py install`

To complete the SPI setup, whilst still in the ZeroSeg directory, run the following command:

`sudo pip install spidev`
