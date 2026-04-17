# ==============================
# Spark MongoDB Project
# ==============================

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from pymongo import MongoClient
import json

# ------------------------------
# 1. Create Spark Session
# ------------------------------
spark = SparkSession.builder.appName("SparkMongoProject").getOrCreate()

# ------------------------------
# 2. Load Data
# ------------------------------
customers = spark.read.csv("D:/Downloads/customers-10000.csv", header=True)
people = spark.read.csv("D:/Downloads/people-10000.csv", header=True)
organizations = spark.read.csv("D:/Downloads/organizations-10000.csv", header=True)

# ------------------------------
# 3. Data Preparation
# ------------------------------
customers = customers.dropDuplicates()
people = people.dropDuplicates()
organizations = organizations.dropDuplicates()

# Convert Subscription Date → Date
customers = customers.withColumn(
    "subscription_date_fixed",
    to_date(col("Subscription Date"), "yyyy-MM-dd")
)

# ------------------------------
# 4. Basic Exploration (Spark)
# ------------------------------
print("Customers count:", customers.count())
print("People count:", people.count())
print("Organizations count:", organizations.count())

# ------------------------------
# 5. Connect to MongoDB Atlas
# ------------------------------
client = MongoClient("mongodb+srv://breakingbadwhalter123_db_user:<QFGVzDeqDeCduEs8>@cluster0.fltnplm.mongodb.net/?appName=Cluster0")

db = client["spark_mango"]

customers_col = db["customers"]
people_col = db["people"]
organizations_col = db["organizations"]

# ------------------------------
# 6. Convert to JSON
# ------------------------------
customers_json = customers.toJSON().collect()
people_json = people.toJSON().collect()
organizations_json = organizations.toJSON().collect()

# ------------------------------
# 7. Insert into MongoDB
# ------------------------------
customers_col.delete_many({})
people_col.delete_many({})
organizations_col.delete_many({})

customers_col.insert_many([json.loads(row) for row in customers_json])
people_col.insert_many([json.loads(row) for row in people_json])
organizations_col.insert_many([json.loads(row) for row in organizations_json])

print("Data inserted into MongoDB successfully ✅")

# ------------------------------
# 8. MongoDB Queries
# ------------------------------

# Customers per country
print("\nCustomers per country:")
for x in customers_col.aggregate([
    {"$group": {"_id": "$Country", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
]):
    print(x)

# Top 5 countries
print("\nTop 5 countries:")
for x in customers_col.aggregate([
    {"$group": {"_id": "$Country", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 5}
]):
    print(x)

# Customers per company
print("\nCustomers per company:")
for x in customers_col.aggregate([
    {"$group": {"_id": "$Company", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
]):
    print(x)

# Earliest & latest subscription
print("\nSubscription dates:")
for x in customers_col.aggregate([
    {
        "$group": {
            "_id": None,
            "earliest": {"$min": "$Subscription Date"},
            "latest": {"$max": "$Subscription Date"}
        }
    }
]):
    print(x)

# ------------------------------
# 9. Stop Spark
# ------------------------------
spark.stop()