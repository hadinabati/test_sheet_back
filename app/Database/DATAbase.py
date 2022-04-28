import motor.motor_asyncio

MONGO_DETAILS = "mongodb://isair_hadi:hadinabati0@91.98.96.171:27017/?authMechanism=DEFAULT&authSource=isair_Users"
# MONGO_DETAILS="mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.isair_Users

userCollection = database.get_collection("userCollection")
student_database = database.get_collection("Students")
# --------------------------------------------------------------
# site_config = client.configs
#
# site_collection = database.get_collection("site_config")

# ----------------------------------------------------------------------

