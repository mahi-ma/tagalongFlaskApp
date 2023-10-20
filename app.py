from flask import Flask
from pymongo import MongoClient

from app import app

if __name__ == '__main__':
    app.run(debug=True)

client = MongoClient('localhost', 27017)
# client = MongoClient('localhost', 27017, username='username', password='password')

db = client.tagalongapp

users = db.users
requests = db.requests
userMappings = db.userMappings