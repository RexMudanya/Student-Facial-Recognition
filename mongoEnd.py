from pymongo import MongoClient
import datetime
import pprint

def databaseConnection():
	client = MongoClient('localhost',27017)
	db=client['FaceRecBase']

#input id and name into database
def inputData(ID,NAME):
	databaseConnection()
	collection=db['credentials']

	post={"id":ID,
	 "name":NAME,
	 "date":datetime.datetime.utcnow()}
	credentials=db.credentials

	if(retrieveData(ID)==True):
		post_id=posts.insert_one(post).insert_id
	else:
		print("ID already exists")

#retrieve data by ID
def retrieveData(ID):
	databaseConnection()
	collection=db['credentials']
	pprint.pprint(posts.find_one({"id":ID}))

#return all documents posted in data
def retrieveAllData():
	databaseConnection()
	posts=db.posts

	for post in posts.find():
		pprint.pprint(post)


#check if an id / name exists in database
def existingData(ID):
	if(retrieveData(ID)):
		return True
	else:
		return False