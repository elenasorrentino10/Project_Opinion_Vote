import redis


def identify_user(r: redis.Redis):
    print('=== User Identification ===')

    email = input('Enter your email: ')
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    user_id = r.get(f'email:{email}')

    if not user_id:
        user_id = r.incr('user_id')

        r.hset(f'user:{user_id}', 'email', email)
        r.hset(f'user:{user_id}', 'username', username)
        r.hset(f'user:{user_id}', 'password', password)

        r.set(f'email:{email}', user_id)
        print('New user created successfully!')
    else:
        user_id = int(user_id)
        user_data = r.hgetall(f'user:{user_id}')

        if user_data[b'username'].decode() != username or \
            user_data[b'password'].decode() != password:
            print('User verification failed. Invalid username or password.')
            return
        
        print(f'User verified with ID: {user_id}')

    return user_id
