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
    BusLine = BusInfo[0]["MonitoredVehicleJourney"]["PublishedLineName"]
    print "Bus Line : %s" %(BusLine)
    count=0
    for Bus in BusInfo:
            Latitude = Bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
            Longitude = Bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
            print 'Bus %d is at latitude %s and longitude %s' % (count, Latitude, Longitude)
            count+=1
    print 'Number of Active buses: %d' %(count)
