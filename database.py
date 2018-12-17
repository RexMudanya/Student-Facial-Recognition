from pymongo import MongoClient
import datetime
import pprint

client = MongoClient('localhost', 27017)

db = client['try']
collection=db['posts']

name = input("Enter Name : ")
id = input("Enter Id : ")


post={"name":name,
	"id":id,
	"date":datetime.datetime.utcnow()}

posts =db.posts

post_id =posts.insert_one(post).inserted_id

pprint.pprint(posts.find_one({"name":name}))