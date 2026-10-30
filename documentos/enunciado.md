# PROYECTO FINAL - DESARROLLO DE SOFTWARE VIII (UTP)

## PROYECTO FINAL - DESARROLLO DE SOFTWARE VIII:

**Valor: 100 puntos**

## 1. Descripción General del Proyecto

Los estudiantes desarrollarán de forma práctica un Sistema IoT Ciberfísico Integrador completo que simule un entorno de monitoreo, control autónomo reactivo y procesamiento distribuido utilizando el simulador Wokwi, la microcomputadora Raspberry Pi Pico W con MicroPython, múltiples sensores, actuadores, almacenamiento local resiliente y una plataforma en la nube. El sistema debe recopilar datos ambientales y físicos en tiempo real, almacenarlos localmente con marcas de tiempo atómicas, procesar eventos mediante programación orientada a eventos (interrupciones de hardware y temporizadores asíncronos), permitir control remoto bidireccional y exponer métricas en la nube.

## 2. Escenario a Implementar

1. Contenedor y Gestionador de Residuos Urbanos ("Smart Waste Management").
2. Seguridad y Ventilación en Minas Subterráneas (Mining Safety IoT).
3. Monitoreo Portuario y Contenedores Refrigerados (Reefer Maritime Logistics).
4. Cadena de Frío Farmacéutica y Registro de Biológicos.
5. Microred Eléctrica e Infraestructura de Carga para Vehículos Eléctricos (Smart EV Charging).

## 3. Requisitos Técnicos Obligatorios

- Mínimo 3 sensores diferentes (ejemplo: temperatura/humedad DHT22, movimiento PIR, luz LDR, potenciómetro analógico ADC).
- Mínimo 3 actuadores diferentes (ejemplo: LEDs indicadoras/RGB, buzzer piezoeléctrico en PWM, servomotor, módulo relé industrial, display LCD 16x2 I2C).
- Código en Python modular y Orientada a Eventos bien documentado
- Manejo de GPIO usando librerías apropiadas
- Lectura de sensores en tiempo real
- Control de actuadores
- Implementar cliente MQTT en el dispositivo [HiveMQ, Mosquitto, o EMQX (Cloud gratuito)].
- Conectar con una base de datos (SQLite local o MySQL/PostgreSQL remota). Almacenar lecturas de sensores con timestamp. Registrar eventos y comandos ejecutados. Implementar consultas para recuperar históricos.
- Plataforma en la Nube, Usar UNA de estas opciones: ThingSpeak (recomendado para comenzar), Adafruit IO, AWS, Azure IoT Hub, Google Cloud IoT. Dashboard de visualización en tiempo real. Recepción de comandos desde la nube hacia el dispositivo.

## 4. Entregables del Proyecto

- Código fuente debidamente estructurado en Github y en el Teams. Incluir, readme, requirements.txt(Especificar los que aportaron en el desarrollo del examen), archivos con los scripts SQL, diagrama de la arquitectura, capturas del circuito y el proyecto zip generado por wokwi.
- Documentación de la arquitectura IoT, diagrama de flujo de datos, configuración de la plataforma Cloud.
- Sustentación oral.

## 5. Criterios de Evaluación

| Aspecto | Peso |
|---|---|
| Funcionamiento completo del sistema | 30% |
| Calidad del código (estructura, comentarios, buenas prácticas) | 10% |
| Integración exitosa de todos los componentes | 5% |
| Documentación | 5% |
| Sustentación | 50% |
