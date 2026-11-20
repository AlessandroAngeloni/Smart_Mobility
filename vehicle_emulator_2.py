import paho.mqtt.client as mqtt
import time
from model.vehicle_descriptor import VehicleDescriptor
from model.electric_vehicle_telemetry_data import ElectricVehicleTelemetryData
from conf.mqtt_conf_params import MqttConfigurationParameters

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def publish_telemetry_data():
    target_topic = "{0}/{1}/{2}/{3}".format(
            MqttConfigurationParameters.MQTT_BASIC_TOPIC,
            MqttConfigurationParameters.VEHICLE_TOPIC,
            vehicle_id,
            MqttConfigurationParameters.VEHICLE_TELEMETRY_TOPIC)
    device_payload_string = electric_vehicle_telemetry_data.to_json()
    mqtt_client.publish(target_topic, device_payload_string, 0, False)
    print(f"Telemetry Data Published: Topic: {target_topic} Payload: {device_payload_string}")

def publish_device_info():
    target_topic = "{0}/{1}/{2}/{3}".format(
                        MqttConfigurationParameters.MQTT_BASIC_TOPIC,
                        MqttConfigurationParameters.VEHICLE_TOPIC,
                        vehicle_descriptor.uuid,
                        MqttConfigurationParameters.VEHICLE_INFO_TOPIC)
    device_payload_string = vehicle_descriptor.to_json()
    mqtt_client.publish(target_topic, device_payload_string, 0, True)
    print(f"Vehicle Info Published: Topic: {target_topic} Payload: {device_payload_string}")

message_limit = 1000

vehicle_id = "python-vehicle-{0}-{1}".format(MqttConfigurationParameters.MQTT_USERNAME,1)

mqtt_client = mqtt.Client(vehicle_id)
mqtt_client.on_connect = on_connect

mqtt_client.username_pw_set(MqttConfigurationParameters.MQTT_USERNAME, MqttConfigurationParameters.MQTT_PASSWORD)

print("Connecting to " + MqttConfigurationParameters.BROKER_ADDRESS + " port: " + str(
    MqttConfigurationParameters.BROKER_PORT))
mqtt_client.connect(MqttConfigurationParameters.BROKER_ADDRESS, MqttConfigurationParameters.BROKER_PORT)

vehicle_descriptor = VehicleDescriptor(vehicle_id, "Tesla", "Model X")

publish_device_info()

mqtt_client.loop_start()
electric_vehicle_telemetry_data = ElectricVehicleTelemetryData()

for message_id in range(message_limit):
    electric_vehicle_telemetry_data.update_measurements(1)
    electric_vehicle_telemetry_data.control(0)
    if(electric_vehicle_telemetry_data.control(0)==1):
        # print("L'autobus è vuoto")
        exit(0)
    publish_telemetry_data()
    time.sleep(1)

mqtt_client.loop_stop()