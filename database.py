from model import User 


# MongoDB driver
import motor.motor_asyncio


# client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")


conn_str = "mongodb+srv://mongotut:testing123@cluster0.kogqa.mongodb.net/TodoListDB?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"

client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=15000)



database = client.EdvoraDB
collection = database.User


async def fetch_one_pokemon(username):
    document = await collection.find_one({"username": username})
    return document 


async def login_user(user):
    document = await collection.find_one({"username": user})
    return document


async def create_user(user):
    document = user
    result = await collection.insert_one(document)
    return document


async def fetch_one_todo(username):
    doc = await collection.find_one({"username": username})
    return doc


async def change_user(user, pokemon):
    await collection.update_one({"username": user}, {"$set": {"pokemon": pokemon}})
    result = await fetch_one_todo(user)
    return result
