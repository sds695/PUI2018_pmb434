from __future__ import print_function
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


#Check number of arguments
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_pmb434.py MTA_API_KEY BUS_LINE")
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
try:
	buses = dataDict["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
except KeyError:
	print("Invalid Bus Line: {}".format(LineRef))
else:
	#Print output
	print ("Bus Line: {}".format(LineRef))

	print ("Number of Active Buses: {}".format(len(buses)))

	for n in range(len(buses)):
		print("Bus {} is at latitude {} and longitude {}".format(
			n+1,
			buses[n]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"],
			buses[n]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
		))