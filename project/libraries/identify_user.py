import redis


def identify_user(r: redis.Redis):
    print('=== User Identification ===')

    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username.encode() not in r.hgetall(f'users'):
        r.hset(f'users', username, password)
        print('New user created successfully!')
    else:
        if password.encode() != r.hget(f'users', username):
            print('Invalid password, try again.')
            return
        
        print(f'\nUser verified successfully! Welcome back {username}!')

    return username
