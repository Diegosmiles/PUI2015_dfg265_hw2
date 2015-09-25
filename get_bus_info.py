#key a69ef6e6-f4ce-4f34-8a9c-5a94139c5f32

import csv
import sys
import json
import urllib2


key= sys.argv[1]
busline= sys.argv[2]

if __name__=='__main__':
    url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" %(key, busline)
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    BusInfo=data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

    with open(sys.argv[2], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude','Stop Name','Stop Status']
        writer.writerow(headers)
        
        for Bus in BusInfo:

    		Latitude = Bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
		Longitude = Bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
		if Bus["MonitoredVehicleJourney"]["OnwardCalls"] == {}:
			Stop = 'N/A'
			Status = 'N/A'
		else:
			Stop = Bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
			Status = Bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]['Extensions']['Distances']["PresentableDistance"]
			row = [Latitude, Longitude, Stop, Status]
			writer.writerow(row)


        
