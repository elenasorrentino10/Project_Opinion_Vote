import redis


def clear_database(r: redis):
    r.flushall()
