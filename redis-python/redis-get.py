import redis
import csv
r = redis.StrictRedis(host='<HOST>',
        port=6379, db=0, password='<KEY>', ssl=False)

print(r.get('<KEY>'))