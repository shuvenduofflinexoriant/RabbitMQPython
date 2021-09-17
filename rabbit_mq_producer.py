import pika
def publish_event_rmq(message,severity):
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='auditlog', exchange_type='topic')
    channel.basic_publish(
        exchange='auditlog', routing_key=severity, body=message)
    print(" [x] Sent %r:%r" % (severity, message))
    connection.close()
