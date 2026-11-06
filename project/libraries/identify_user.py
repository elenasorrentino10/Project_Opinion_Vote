from getpass import getpass

import redis

from libraries.passwords import hash_password, verify_password


def identify_user(r: redis.Redis):
    print('=== User Identification ===')

    username = input('Enter your username: ')
    password = getpass('Enter your password: ')

    stored_password = r.hget('users', username)

    if stored_password is None:
        r.hset('users', username, hash_password(password))
        print('New user created successfully!')
    else:
        if not verify_password(password, stored_password.decode()):
            print('Invalid password, try again.')
            return

        print(f'\nUser verified successfully! Welcome back {username}!')

    return username
