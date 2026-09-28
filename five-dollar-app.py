from flask import Flask, send_from_directory
from pymongo import MongoClient

app = Flask(__name__)

# yusuncs_db_user
# o4wxEXvoM8YZ6Vvo

MONGO_URL =  "mongodb+srv://yusuncs_db_user:o4wxEXvoM8YZ6Vvo@cluster0.rwby9dy.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URL)
db = client["food_db"]
foods_collection = db["foods"]

local_db = [
    {
        "name" : "Pizza",
        "price" : 6.99,
    },
    {
        "name" : "Panda Express",
        "price" : 11.99,
    },
    {
        "name" : "Subway",
        "price" : 8.99,
    },
    {
        "name" : "Starbucks",
        "price" : 5.99,
    }
]

# Add initial data to MongoDB only if the collection is empty
if foods_collection.count_documents({}) == 0:
    foods_collection.insert_many(local_db)

@app.route("/search/<budget>")
def search_food_items(budget):
    budget = float(budget)
    res = []
    for food_item in local_db:
        if food_item['price'] <= budget:
            res.append(food_item)
    return res

@app.route("/search_mongo/<budget>")
def search_food_items_mongo(budget):

    budget = float(budget)
    foods = foods_collection.find(
        {"price": {"$lte": budget}},
        {"_id": 0}
    )
    return list(foods)

@app.route("/hello")
def hello_world():
    return "Hello World from CS4800!"

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

app.run(host = "0.0.0.0", port = 5050)