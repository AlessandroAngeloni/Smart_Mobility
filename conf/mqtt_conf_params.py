class MqttConfigurationParameters(object):

    BROKER_ADDRESS = "155.185.228.20"
    BROKER_PORT = 7883
    MQTT_USERNAME = "273048@studenti.unimore.it"
    MQTT_PASSWORD = "wvlwcyibdezzkvse"
    MQTT_BASIC_TOPIC = "/iot/user/273048@studenti.unimore.it".format(MQTT_USERNAME)
    VEHICLE_TOPIC = "vehicle"
    VEHICLE_TELEMETRY_TOPIC = "telemetry"
    VEHICLE_INFO_TOPIC = "info"