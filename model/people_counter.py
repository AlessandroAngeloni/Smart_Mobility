import json

class PeopleCounter:

    def __init__(self,peopleBus,peopleIn,peopleOut):
        self.peopleBus=peopleBus
        self.peopleIn=peopleIn
        self.peopleOut=peopleOut

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)