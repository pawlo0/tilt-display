import blescan
import sys
import time
from datetime import datetime 
import bluetooth._bluetooth as bluez

#Assign uuid's of various colour tilt hydrometers. BLE devices like the tilt work primarily using advertisements. 
#The first section of any advertisement is the universally unique identifier. Tilt uses a particular identifier based on the colour of the device
red    	= 'a495bb10c5b14b44b5121370f02d74de'
green  	= 'a495bb20c5b14b44b5121370f02d74de'
black  	= 'a495bb30c5b14b44b5121370f02d74de'
purple 	= 'a495bb40c5b14b44b5121370f02d74de'
orange 	= 'a495bb50c5b14b44b5121370f02d74de'
blue   	= 'a495bb60c5b14b44b5121370f02d74de'
yellow 	= 'a495bb70c5b14b44b5121370f02d74de'
pink   	= 'a495bb80c5b14b44b5121370f02d74de'

#The default device for bluetooth scan. If you're using a bluetooth dongle you may have to change this.
dev_id = 0

#scan BLE advertisements until we see one matching our tilt uuid
def getdata():
	try:
		sock = bluez.hci_open_dev(dev_id)

	except:
		print "error accessing bluetooth device..."
		sys.exit(1)

	blescan.hci_le_set_scan_parameters(sock)
	blescan.hci_enable_le_scan(sock)

	gotData = 0

	while (gotData == 0):

		returnedList = blescan.parse_events(sock, 10)

		for beacon in returnedList: #returnedList is a list datatype of string datatypes seperated by commas (,)
			output = beacon.split(',') #split the list into individual strings in an array
			if output[1] == blue: #Change this to the colour of you tilt
				tempf = float(output[2]) #convert the string for the temperature to a float type

				gotData = 1
				tiltSG = float(output[3])/1000
				tiltTemp = tempf

	#assign values to a dictionary variable for the http POST to google sheet
	data= 	{
			"Time": datetime.now(),
			'SG': tiltSG,
			'Temp': tiltTemp,
			}
	blescan.hci_disable_le_scan(sock)
	return data


def main():

	while True:
		data = getdata()
		print "SG/Concentration: ",data["SG"]," Temperature: ",(data["Temp"]-32)*5/9,"C"
		print "at ", str(data["Time"])

if __name__ == "__main__": #dont run this as a module
	main()
