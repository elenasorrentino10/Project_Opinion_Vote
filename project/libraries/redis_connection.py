import os

import redis


def redis_connection():
    try:
        host = os.environ['REDIS_HOST']
        port = int(os.environ['REDIS_PORT'])
        password = os.environ['REDIS_PASSWORD']

    except KeyError as missing:
        print(f'Missing environment variable: {missing}. See step 4 of "Getting Started" in the README.')
        exit(-1)

    except ValueError:
        print('REDIS_PORT must be a number.')
        exit(-1)

    try:

        connection = redis.Redis(
            host=host,
            port=port,
            password=password
        )

        connection.ping()
        return connection

    except redis.exceptions.AuthenticationError:
        # print('Errore di autenticazione al server redis!')
        print('Redis server Authentification Error!')
        exit(-1)

    except redis.exceptions.ConnectionError:
        print('Redis server Connection Error!')
        # print('Errore di connessione al server redis!')
        exit(-1)
