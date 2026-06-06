import logging
import random
import time

from message_queue_simulator.consumer import Consumer
from message_queue_simulator.message import Message
from message_queue_simulator.message_queue import MessageQueue
from message_queue_simulator.priority import Priority
from message_queue_simulator.producer import Producer

# Ahora Python encontrará esto sin problemas

# Configuramos el formato del logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)

logger = logging.getLogger(__name__)


def create_random_message() -> Message:
    """Fábrica para crear mensajes con prioridades aleatorias."""
    priorities = list(Priority)
    return Message(
        payload={"data": f"random_value_{random.randint(1, 100)}"},
        priority=random.choice(priorities),
    )


def handle_message(message: Message) -> None:
    """Simula el procesamiento de un mensaje consumiendo un poco de tiempo."""
    time.sleep(0.02)


def main() -> None:
    logger.info("Starting Message Queue Simulator...")

    # Creamos una cola con capacidad máxima de 10
    queue = MessageQueue(max_size=10)

    # Creamos 2 Productores y 2 Consumidores
    producers = [Producer(queue, create_random_message) for _ in range(2)]
    consumers = [Consumer(queue, handle_message) for _ in range(2)]

    logger.info("Starting threads...")
    for c in consumers:
        c.start()
    for p in producers:
        p.start()

    # Dejamos correr el simulador por 2 segundos
    time.sleep(2)

    logger.info("Stopping threads...")
    for p in producers:
        p.stop()
    for c in consumers:
        c.stop()

    # Reporte final
    total_produced = sum(p.produced_count() for p in producers)
    total_consumed = sum(c.processed_count() for c in consumers)
    print("\n")
    logger.info("=== SIMULATION RESULTS ===")
    logger.info(f"Total Messages Produced: {total_produced}")
    logger.info(f"Total Messages Consumed: {total_consumed}")
    logger.info(f"Messages left in Queue: {queue.size()}")
    logger.info("Simulation finished successfully.")


if __name__ == "__main__":
    main()
