# 🔥 Spark MongoDB Project

A data engineering pipeline that uses **Apache Spark** for large-scale data processing and **MongoDB Atlas** for storage, querying, and visualization. Built as a team project demonstrating end-to-end ETL with analytical insights across three real-world datasets.

---

## 👥 Team Members

| Name |
|------|
| Mohab Badawy |
| Mohamed Tarek |
| Youssef ElShazly |
| Salma Ahmed Hassan |
| Menna Al-Zahaby |
| Samira Gamal |


---

## 📌 Project Overview

This project demonstrates a full data pipeline:

1. Load and clean CSV datasets using **PySpark**
2. Store the processed data into **MongoDB Atlas** collections
3. Run aggregation queries on the stored data
4. Visualize insights using bar charts, pie charts, and line charts

---

## 🗂️ Repository Structure

```
Spark-MongoDB-Project/
│
├── spark-py.py                     # Main pipeline script (Spark + MongoDB)
├── connect.ipynb                   # Jupyter notebook version of the pipeline
├── requirements.txt                # Python dependencies
│
├── customers-10000.csv             # Customer dataset (10,000 records)
├── people-10000.csv                # People dataset (10,000 records)
├── organizations-10000.csv         # Organizations dataset (10,000 records)
│
├── Bar Chart.jpeg                  # Customers per country
├── Bar Chart (2).jpeg              # Customers per company
├── Pie chart.jpeg                  # Gender distribution
├── Line Chart.jpeg                 # Subscription trends over time
│
└── Predictive_Churn_Analytics.pdf  # Full project report
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Apache Spark / PySpark** | Distributed data loading, cleaning, and transformation |
| **MongoDB Atlas** | Cloud NoSQL storage and aggregation queries |
| **PyMongo** | Python driver for MongoDB |
| **Matplotlib / Seaborn** | Data visualization |
| **Jupyter Notebook** | Interactive development environment |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Java 8 or 11 (required by Apache Spark)
- A [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) account with a cluster set up

### Installation

```bash
# Clone the repository
git clone https://github.com/mohamedtarek750/Spark-MongoDB-Project.git
cd Spark-MongoDB-Project

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Before running, update the MongoDB connection string in `spark-py.py`:

```python
client = MongoClient("mongodb+srv://<username>:<password>@<cluster>.mongodb.net/")
```

Also update the CSV file paths to match your local environment:

```python
customers = spark.read.csv("/path/to/customers-10000.csv", header=True)
people    = spark.read.csv("/path/to/people-10000.csv", header=True)
organizations = spark.read.csv("/path/to/organizations-10000.csv", header=True)
```

### Run the Pipeline

```bash
python spark-py.py
```

Or open the interactive notebook:

```bash
jupyter notebook connect.ipynb
```

---

## 🔄 Pipeline Walkthrough

### 1. Load Data
Three CSV files are loaded into Spark DataFrames — customers, people, and organizations (10,000 records each).

### 2. Data Preparation
- Duplicates are removed with `.dropDuplicates()`
- The `Subscription Date` column is cast to a proper `DateType` for time-series analysis

### 3. Store in MongoDB Atlas
DataFrames are serialized to JSON and inserted into three MongoDB collections: `customers`, `people`, and `organizations`. Collections are cleared before each run to ensure idempotency.

### 4. MongoDB Aggregation Queries

| Query | Description |
|-------|-------------|
| Customers per country | Groups and counts customers by country, sorted descending |
| Top 5 countries | Same as above, limited to top 5 |
| Customers per company | Groups customers by their associated company |
| Subscription date range | Finds the earliest and latest subscription dates |

### 5. Visualization
Charts are generated from query results:

- **Bar Chart** — Customer distribution by country
- **Bar Chart (2)** — Customer distribution by company
- **Pie Chart** — Gender breakdown
- **Line Chart** — Subscription trends over time

---

## 📊 Sample Visualizations

| Chart | Preview |
|-------|---------|
| Customers by Country | ![Bar Chart](Bar%20Chart.jpeg) |
| Customers by Company | ![Bar Chart 2](Bar%20Chart%20(2).jpeg) |
| Gender Distribution | ![Pie Chart](Pie%20chart.jpeg) |
| Subscription Trends | ![Line Chart](Line%20Chart.jpeg) |

---

## 📄 Project Report

A detailed writeup covering methodology, findings, and predictive churn analytics is available in [`Predictive_Churn_Analytics.pdf`](Predictive_Churn_Analytics.pdf).

---

## ⚠️ Security Notice

The MongoDB connection string in `spark-py.py` contains credentials that were committed to the repository. **These should be rotated immediately.** For future use, store secrets in environment variables:

```python
import os
from pymongo import MongoClient

client = MongoClient(os.environ["MONGO_URI"])
```

---

## 📦 Dependencies

```
pymongo
pyspark
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 📝 License

This project was developed for academic purposes. No license has been specified.
