import pymongo
import csv

client = pymongo.MongoClient(
   "<CONNECTION STRING>", ssl=True,ssl_cert_reqs='CERT_NONE')

db = client['<DATABASE>']
empregados = db['<COLLECTION>']

obj = {}

empregados.insert_one(obj)
