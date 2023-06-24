import redis


def flush_database(r: redis.Redis):
    confirm = input("Are you sure you want to clear the database? This action cannot be undone. (y/n): ")
    if confirm.lower() == 'y':
        r.flushall()
        print("Database cleared successfully!")
    else:
        print("Clear database operation canceled.")
