import json
import gpxpy.gpx

class GeoLocation:

    def __init__(self,latitude,longitude):
        self.latitude=latitude
        self.longitude=longitude

    def location(self,fermata,loc):
        gpx_file = open('tracks/gpxWaypointVehicle.gpx', 'r')
        gpx = gpxpy.parse(gpx_file)
        if(loc==0):
            waypoint=gpx.waypoints[fermata]
        elif(loc==1):
            waypoint = gpx.waypoints[-fermata]
        else:
            waypoint = gpx.waypoints[fermata+30]

        return waypoint.latitude, waypoint.longitude


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)