from project.resources.connection_data import host, port, password
import redis


def redis_connection():
    try:

        connection = redis.Redis(
            host=host,
            port=port,
            password=password
        )

        connection.ping()
        return connection

    except redis.exceptions.AuthenticationError:
        print('Errore di autenticazione al server redis!')
        exit(-1)

    except redis.exceptions.ConnectionError:
        print('Errore di connessione al server redis!')
        exit(-1)
