import redis


def delete_user(user_id: int, r: redis.Redis):
    user_key = f'user:{user_id}'
    user_data = r.hgetall(user_key)

    email = user_data[b'email'].decode()
    messages_key = f'messages:{user_id}'

    r.delete(user_key, f'email:{email}', messages_key)
    print("User deleted successfully!")
