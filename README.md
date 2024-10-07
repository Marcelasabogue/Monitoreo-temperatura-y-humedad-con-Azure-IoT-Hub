# Proyecto_IoT--Monitoreo_temperatura_y_humedad
Creacion de un sistema que simula el monitoreo de temperatura y humedad en tiempo real, utilizando Azure IoT Hub para recibir datos simulados de sensores y Apache Spark para el análisis de esos datos.

1. **Simulador de Dispositivos IoT:** Emplea una simulacion de dispositivo para generar generando datos aleatorios de forma continua para los parametros de temperatura y humedad.
2. **Configura Azure IoT Hub:** Establece un Azure IoT Hub para recibir los datos simulados de los dispositivos. 
3. **Implementa Azure Stream Analytics:** Configura un proceso en Azure Stream Analytics que permita procesar los datos en tiempo real a medida que llegan desde el IoT Hub.
4. **Configura Apache Spark en Azure Databricks:** Establece un clúster en Azure Databricks para almacenar y analizar los datos recolectados.
5. **Almacenamiento de Datos:** Utiliza Azure Blob Storage para guardar los datos históricos generados por los dispositivos.
6. **Crea un Dashboard en Power BI:** Diseña un dashboard que muestre los datos de temperatura y humedad en tiempo real.
7. **Configura Alertas:** Establece notificaciones para alertar sobre condiciones extremas de temperatura o humedad, garantizando una respuesta rápida ante situaciones críticas.

