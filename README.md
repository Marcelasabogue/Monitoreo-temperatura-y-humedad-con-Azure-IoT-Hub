# Proyecto IoT: Monitoreo de Temperatura y Humedad

Este proyecto implementa un sistema para el monitoreo en tiempo real de temperatura y humedad, utilizando Azure IoT Hub para recibir datos provenientes de el sistema de simulación, Azure Stream Analytics para su análisis y azure Blob Storage para guardar los datos.

![Arquitectura del proyecto](Imagenes/arquitecturaiot.png)


## Contenido del Proyecto

1. **Simulador de Dispositivos IoT**:
   - Genera datos aleatorios de temperatura y humedad de forma continua.

2. **Configuración de Azure IoT Hub**:
   - Configura el IoT Hub para recibir datos de los dispositivos simulados.

3. **Implementación de Azure Stream Analytics**:
   - Procesa los datos en tiempo real a medida que llegan desde el IoT Hub.

4. **Almacenamiento de Datos**:
   - Utiliza Azure Blob Storage para guardar los datos 

