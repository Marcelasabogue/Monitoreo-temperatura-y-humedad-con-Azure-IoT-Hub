# Proyecto IoT: Monitoreo de Temperatura y Humedad

Este proyecto crea un sistema que simula el monitoreo de temperatura y humedad en tiempo real. Utiliza Azure IoT Hub para recibir datos simulados de sensores y Apache Spark para el análisis de esos datos.

## Contenido del Proyecto

1. **Simulador de Dispositivos IoT**: 
   - Emplea un simulador de dispositivos para generar datos aleatorios de forma continua para los parámetros de temperatura y humedad.

2. **Configuración de Azure IoT Hub**: 
   - Establece un Azure IoT Hub para recibir los datos simulados de los dispositivos.

3. **Implementación de Azure Stream Analytics**: 
   - Configura un proceso en Azure Stream Analytics que permite procesar los datos en tiempo real a medida que llegan desde el IoT Hub.

4. **Configuración de Apache Spark en Azure Databricks**: 
   - Establece un clúster en Azure Databricks para almacenar y analizar los datos recolectados.

5. **Almacenamiento de Datos**: 
   - Utiliza Azure Blob Storage para guardar los datos históricos generados por los dispositivos.

6. **Creación de un Dashboard en Power BI**: 
   - Diseña un dashboard que muestre los datos de temperatura y humedad en tiempo real.

7. **Configuración de Alertas**: 
   - Establece notificaciones para alertar sobre condiciones extremas de temperatura o humedad, garantizando una respuesta rápida ante situaciones críticas.

## Tecnologías Utilizadas

- **Azure IoT Hub**
- **Azure Stream Analytics**
- **Apache Spark**
- **Azure Databricks**
- **Azure Blob Storage**
- **Power BI**

## Requisitos Previos

- Cuenta de Azure
- Conocimientos básicos de programación en Python (opcional, dependiendo del simulador)
- Acceso a Power BI

## Instalación y Configuración

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/Marcelasabogue/Proyecto-IoT---Monitoreo-temperatura-y-humedad.git
   cd Proyecto-IoT---Monitoreo-temperatura-y-humedad
