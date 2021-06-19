import redis
import csv
r = redis.StrictRedis(host='<HOST>',
        port=6379, db=0, password='<SECRET>', ssl=False)

key = "<KEY>"
value = str("<VALUE>")

r.set(key, value)

#r.delete('789-guilherme-piccin')