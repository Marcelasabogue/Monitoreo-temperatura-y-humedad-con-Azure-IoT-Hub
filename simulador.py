import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

# Reemplaza con tu cadena de conexión del IoT Hub
connection_string = "<tu_connection_string>"
client = IoTHubDeviceClient.create_from_connection_string(connection_string)

def generate_random_data():
    """Genera datos aleatorios de temperatura y humedad."""
    temperature = random.uniform(15.0, 30.0)  # Temperatura en °C
    humidity = random.uniform(30.0, 70.0)      # Humedad en %
    return {
        "deviceId": "simulatedDevice",
        "temperature": round(temperature, 2),
        "humidity": round(humidity, 2)
    }

try:
    while True:
        data = generate_random_data()
        message = Message(str(data))
        client.send_message(message)
        print(f"Sent message: {data}")
        time.sleep(5)  # Envía cada 5 segundos
except KeyboardInterrupt:
    print("Simulación detenida.")
finally:
    client.shutdown()
