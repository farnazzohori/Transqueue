import random
import time


def get_transaction_code():
    random_value = str(random.randint(0,10000000000))
    timestamp = str(time.time()).replace(".","")
    return str(timestamp + random_value)

print(get_transaction_code())