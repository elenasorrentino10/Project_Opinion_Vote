import redis


def delete_user(username: str, r: redis.Redis):
    confirm = input("Are you sure you want to delete your account? This action cannot be undone. (y/n): ")
    if confirm.lower() == 'y':
        r.hdel('users', username)
        print("User deleted successfully!")
    else:
        print("User delete operation canceled.")
