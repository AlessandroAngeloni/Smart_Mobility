import json

class VehicleDescriptor:

    def __init__(self, uuid, manufacturer, model):
        self.uuid = uuid
        self.manufacturer = manufacturer
        self.model = model

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)