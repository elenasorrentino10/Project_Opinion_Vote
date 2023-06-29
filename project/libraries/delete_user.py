import redis


def delete_user(user_id: int, r: redis.Redis):
    confirm = input("Are you sure you want to delete your account? This action cannot be undone. (y/n): ")
    if confirm.lower() == 'y':
        user_key = f'user:{user_id}'
        user_data = r.hgetall(user_key)

        email = user_data[b'email'].decode()
        messages_key = f'messages:{user_id}'

        r.delete(user_key, f'email:{email}', messages_key)
        print("User deleted successfully!")
    else:
        print("User delete operation canceled.")
