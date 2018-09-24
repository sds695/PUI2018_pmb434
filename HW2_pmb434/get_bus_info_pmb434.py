from __future__ import print_function
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


#Check number of arguments
if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python show_bus_locations_pmb434.py MTA_API_KEY BUS_LINE FILE_NAME.csv")
    sys.exit()


#Set parameters
key = sys.argv[1]
LineRef = sys.argv[2].upper()
version = "2"

#Set API endpoint
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={}&version={}&LineRef={}".format(key, version, LineRef)

#Read data
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

#Get buses array
if "ErrorCondition" in dataDict["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0].keys():
	#Print error from API
	print(dataDict["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["ErrorCondition"]["Description"])
else:
	#Get buses
	buses = dataDict["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

	#Open file
	fout = open(sys.argv[3], "w")
	
	#Print output
	fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

	for bus in buses:

		#Check for empty MonitoredCall
		if bus["MonitoredVehicleJourney"]["MonitoredCall"]:
			fout.write("{},{},{},{}\n".format(
				bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"],
				bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"],
				bus["MonitoredVehicleJourney"]["MonitoredCall"]["StopPointName"][0],
				bus["MonitoredVehicleJourney"]["MonitoredCall"]["ArrivalProximityText"]
			))
		else:
			fout.write("{},{},{},{}\n".format(
				bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"],
				bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"],
				"N/A",
				"N/A"
			))

	fout.close()

	print("{} bus info written to {}".format(LineRef,sys.argv[3]))