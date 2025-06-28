# 📡 Real-Time Retail Data Pipeline: End-to-End Cloud Architecture

This project simulates and processes real-time retail orders with a fully orchestrated cloud-native architecture.

Data flows from a **web uploader or Python generator → Amazon S3 → Databricks (for transformation) → Snowflake (as data warehouse) → Power BI (for visualization)** — all automated via **Dockerized Apache Airflow**.

---

## ⚙️ Key Features

- 🔁 Real-time data ingestion via Kinesis Firehose  
- 🧾 CSV data upload through a web interface  
- 🔄 Transformations handled by Databricks (PySpark)  
- 📂 Raw and Processed storage in Amazon S3  
- 🧊 Final warehousing in Snowflake  
- 📊 BI Dashboards using Power BI  
- 🐳 Automated workflows containerized with Docker  
- 🗂️ Orchestration handled via Apache Airflow DAGs  


---

## 🛠️ Tech Stack

| Layer              | Tools Used                             |
|--------------------|-----------------------------------------|
| Ingestion           | Python, Web App, AWS Kinesis Firehose  |
| Staging & Storage   | Amazon S3 (raw-zone & processed-zone)  |
| Transformation      | Databricks (Apache Spark, PySpark)     |
| Orchestration       | Apache Airflow (Dockerized)            |
| Data Warehouse      | Snowflake                              |
| BI & Visualization  | Power BI                               |

---

## 🚀 Setup Instructions

1. **Upload CSV Data**  
   - Use the web interface or `python_realtime_generator.py`

2. **Raw Storage on S3**  
   - Uploads store data in CSV format to the raw-zone

3. **Databricks Transformation**  
   - Transforms data and writes to processed-zone in S3

4. **Load into Snowflake**  
   - Uses `COPY INTO` SQL for efficient loading

5. **Visualize in Power BI**  
   - Connect Power BI to Snowflake for live dashboards

6. **Automation**  
   - All steps orchestrated with Dockerized Airflow DAGs

---

---

## 📊 Dashboard Sample

Power BI displays:

- ✅ Total Orders  
- 🏬 Store-wise Sales  
- 💵 Revenue Trends  
- 📦 Item-wise Distribution  
- ⏱️ Real-time timestamps  

---

## 💡 Learning Outcomes

- 🔧 Built an end-to-end real-time data pipeline  
- 🧠 Understood lakehouse architecture  
- 🤖 Automated ETL workflows using Airflow  
- ⚡ Implemented real-time ingestion via Kinesis Firehose  
- 📈 Visualized clean data in Power BI  

---

## 🙏 Acknowledgements

Thanks to:

- 🌐 AWS Free Tier  
- 🔥 Databricks Community Edition  
- ❄️ Snowflake Free Trial  
- 💙 Stack Overflow  

---

## 📬 Connect with Me

- 🔗 [LinkedIn](https://www.linkedin.com/in/siva-sandeep/)

---

## 🏷️ Tags

`#AWS` `#Snowflake` `#Databricks` `#Docker` `#Airflow` `#Kinesis` `#S3` `#PowerBI`  
`#Python` `#ETL` `#DataEngineering` `#RealTimeAnalytics`
