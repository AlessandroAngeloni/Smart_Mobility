import json
import random
import time
from model.geo_location import GeoLocation
from model.people_counter import PeopleCounter

class ElectricVehicleTelemetryData:

    def __init__(self):
        self.batteryLevel = 100.0
        self.geoLocation = GeoLocation(0.0, 0.0)
        self.peopleCounter= PeopleCounter(15 + int(random.uniform(0.0, 10.0)),0,0) # peopleBus negativo
        self.inDoor=True
        self.outDoor=True
        self.avanti=True
        self.fermata=0  # indici sfalsati
        self.timestamp = int(time.time())

    def update_measurements(self,loc):
        people_bus=self.peopleCounter.peopleBus+self.peopleCounter.peopleIn-self.peopleCounter.peopleOut
        latitude,longitude=GeoLocation.location(0,self.fermata,loc)

        self.batteryLevel = self.batteryLevel - random.uniform(0.0, 5.0)
        self.peopleCounter=PeopleCounter(people_bus,int(random.uniform(0.0,10.0)),int(random.uniform(0.0,10.0)))
        self.geoLocation = GeoLocation(latitude,longitude)
        self.fermata+=1
        self.timestamp = int(time.time())

    def control(self,empty):
        if(self.peopleCounter.peopleBus>30):
            # print("Troppe persone sull'autobus")
            self.peopleCounter.peopleIn=0
            self.inDoor=False
        else:
            self.inDoor=True

        if(self.batteryLevel<10):
            # print("Batteria scarica")
            self.peopleCounter.peopleIn = 0
            self.inDoor = False
            if(self.peopleCounter.peopleBus<=0 or self.batteryLevel<0):
                self.peopleCounter.peopleOut = 0
                self.outDoor = False
                # print("L'autobus è vuoto")
                empty=1
                return empty

        if(self.fermata==1):
            self.avanti=True
        elif(self.fermata==6):
            self.avanti=False

        if(not(self.avanti)):
            self.fermata -= 1

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)