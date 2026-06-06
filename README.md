# Simulador de Cola de Mensajes (Message Queue Simulator)

Un simulador concurrente de colas de mensajes implementado en Python. Este proyecto fue desarrollado para demostrar la aplicación de principios avanzados de ingeniería de software, incluyendo concurrencia (multithreading), manejo de contrapresión (backpressure) y la metodología de Desarrollo Guiado por Pruebas (TDD).

## 🚀 Características Principales

* **Patrón Productor-Consumidor**: Implementado utilizando el módulo `threading` de Python para simular la producción y el consumo de mensajes de manera concurrente.
* **Cola de Prioridad**: Los mensajes se procesan según su nivel de prioridad (ALTA, MEDIA, BAJA) utilizando una `PriorityQueue` segura para hilos. Se garantiza el orden FIFO (First-In-First-Out) para los mensajes que comparten la misma prioridad.
* **Manejo de Contrapresión (Backpressure)**: La cola de mensajes (`MessageQueue`) soporta una capacidad máxima configurable. Los productores manejan la excepción `QueueFullError` de forma elegante (pausando su ejecución), lo que previene el desbordamiento de memoria.
* **Manejo de Inactividad (Idle Handling)**: Los consumidores manejan la excepción `QueueEmptyError` de manera segura, esperando por nuevos mensajes sin que el hilo colapse.
* **Observabilidad en Tiempo Real**: El sistema integra el módulo estándar de `logging` para registrar exactamente cuándo se producen, consumen o rechazan los mensajes, finalizando con un reporte de métricas de la simulación.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje**: Python 3.14+
* **Gestor de Dependencias**: [Poetry](https://python-poetry.org/)
* **Testing**: Pytest (100% de cobertura en tests construidos con estricta metodología Red-Green-Refactor).
* **Calidad de Código**: Black (Formateo) y Ruff (Linter y orden de imports).

## 🏗️ Estructura del Proyecto

El proyecto sigue un diseño Orientado a Objetos limpio y desacoplado:
* `Message`: Clase de datos (dataclass) inmutable que representa una tarea con un UUID único y una prioridad.
* `MessageQueue`: Cola de prioridad segura para hilos con configuración de capacidad máxima.
* `Producer`: Hilo en segundo plano encargado de generar y encolar mensajes.
* `Consumer`: Hilo en segundo plano encargado de extraer y procesar mensajes.

## 💻 Cómo Ejecutar el Proyecto

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Matute0512/message-queue-simulator.git
   cd message-queue-simulator
   ```

2. **Instalar dependencias utilizando Poetry:**
   ```bash
   poetry install
   ```

3. **Ejecutar la simulación:**
   ```bash
   poetry run python src/main.py
   ```

## 🧪 Ejecutar Tests y Herramientas de Calidad

Este proyecto fue construido usando TDD. Para ejecutar la suite de pruebas y verificar la calidad del código, puedes usar los siguientes comandos:

```bash
# Ejecutar la suite de pruebas (Pytest)
poetry run pytest

# Ejecutar el formateador de código (Black)
poetry run black .

# Ejecutar el linter para encontrar errores (Ruff)
poetry run ruff check .
```