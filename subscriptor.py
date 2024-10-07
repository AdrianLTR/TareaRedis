import redis

# Configuración de Redis
redis_host = 'redis-13550.c61.us-east-1-3.ec2.redns.redis-cloud.com'
redis_port = 13550
redis_password = 'IRUci0FnJPBzrjpLHLDafZFAXhkSAiGo'

# Conexión a Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Suscriptor
def subscriber():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('canal_prueba')
    
    print("Esperando mensajes...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Recibido: {message['data']}")

if __name__ == "__main__":
    subscriber()
