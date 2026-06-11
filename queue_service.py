from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os


class QueueService:

    def __init__(self):

        self.client = ServiceBusClient.from_connection_string(
            os.getenv("SERVICE_BUS_CONNECTION")
        )

        self.queue_name = os.getenv("QUEUE_NAME")

    def enqueue(self, payload):

        with self.client.get_queue_sender(
            self.queue_name
        ) as sender:

            sender.send_messages(
                ServiceBusMessage(str(payload))
            )