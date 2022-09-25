import pika


class Consumer:
    def __init__(self):
        self.__url = '183.99.87.90'
        self.__port = 5672
        self.__vhost = '/'
        self.__cred = pika.PlainCredentials('guest', 'guest')
        self.__queue = 'InGi';

    def on_message(channel, method_frame, header_frame, body):
        print('Received %s' % body.decode())

    def main(self):
        conn = pika.BlockingConnection(pika.ConnectionParameters(self.__url, self.__port, self.__vhost, self.__cred))
        chan = conn.channel()
        chan.basic_consume(queue=self.__queue, on_message_callback=Consumer.on_message, auto_ack=True)
        print('Consumer is starting...')
        chan.start_consuming()


consumer = Consumer()
consumer.main()